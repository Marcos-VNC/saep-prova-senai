export const state = () => ({
  BASE_URL: "http://localhost:8000",
  User: {},
});

export const mutations = {
  STORE_SESSION(state, payload) {
    state.User = payload;
  },
};
