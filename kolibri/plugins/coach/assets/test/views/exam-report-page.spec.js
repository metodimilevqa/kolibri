/* eslint-env mocha */
import assert from 'assert';
import Vue from 'vue-test'; // eslint-disable-line
import Vuex from 'vuex';
import { mount } from '@vue/test-utils';
import ExamReportPage from '../../src/views/exams/exam-report-page';

function makeWrapper(options = {}) {
  return mount(ExamReportPage, { ...options, stubs: ['kRouterLink', 'assignmentSummary'] });
}

function getElements(wrapper) {
  return {
    averageScore: () => wrapper.find('.average-score'),
    tableRows: () => wrapper.findAll('tbody > tr'),
  };
}

// prettier-ignore
function getTextInScoreColumn(tdEl) {
  // in the fourth column
  return tdEl.findAll('td').at(3).text();
}

const initialState = () => ({
  classId: 'class_1',
  pageState: {
    channelId: 'channel_1',
    examTakers: [],
    exam: {
      question_count: 6,
    },
    learnerGroups: [],
  },
});

describe('exam report page', () => {
  it('average score is not shown if no exams are in progress', () => {
    const state = initialState();
    state.pageState.examTakers = [
      { progress: undefined, group: {}, score: undefined },
      { progress: undefined, group: {}, score: undefined },
    ];
    const wrapper = makeWrapper({ store: new Vuex.Store({ state }) });
    const { averageScore } = getElements(wrapper);
    assert(
      !averageScore()
        .text()
        .trim()
        .endsWith('%')
    );
  });

  it('average score is shown if at least one exam in progress', () => {
    const state = initialState();
    state.pageState.examTakers = [
      { progress: 6, group: {}, score: 3 },
      { progress: 6, group: {}, score: 3 },
      { progress: undefined, group: {}, score: undefined },
    ];
    const wrapper = makeWrapper({ store: new Vuex.Store({ state }) });
    const { averageScore } = getElements(wrapper);
    assert(
      averageScore()
        .text()
        .trim()
        .endsWith('%')
    );
  });

  it('shows correct scores for exam takers', () => {
    const state = initialState();
    state.pageState.examTakers = [
      { progress: 6, group: {}, score: 3 },
      { progress: undefined, group: {}, score: undefined },
    ];
    const wrapper = makeWrapper({ store: new Vuex.Store({ state }) });
    const { tableRows } = getElements(wrapper);
    // score is properly formatted
    assert.equal(getTextInScoreColumn(tableRows().at(0)).trim(), '50%');
    // emdash
    assert.equal(getTextInScoreColumn(tableRows().at(1)).trim(), '–');
  });
});
