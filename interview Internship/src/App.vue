<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <div id="app">
    <h2>To-Do List</h2>
    <input v-model="newTask" placeholder="Add a new task" />
    <button @click="addTask">Add</button>

    <ul>
      <li v-for="(task, index) in taskList" :key="index">{{ task.text }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTask: "",
      taskList: [],
    };
  },
  methods: {
    addTask() {
      if (this.newTask.trim() !== "") {
        this.taskList.push({ text: this.newTask });
        this.newTask = "";
      }
    },
  },
};
</script>

<style>
#app {
  font-family: 'Arial', sans-serif;
  text-align: center;
  padding: 20px;
}

input {
  padding: 8px;
  margin-right: 8px;
}

button {
  padding: 8px;
  cursor: pointer;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 8px;
}
</style>
