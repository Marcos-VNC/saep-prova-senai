<template>
  <main class="main">
    <div class="header">
      <img src="techman.png" alt="" />
      <div class="nav-buttons">
        <div v-if="user.data[0].perfilFK == 2" class="new">
          Novo equipamento
        </div>
        <img @click="logout" src="logout_sair.png" alt="" />
      </div>
    </div>
    <div class="content">
      <div
        v-for="(device, id) in devices"
        :key="id"
        class="equips flexRowCenter"
      >
        <div class="image">
          <img :src="base_url + device.image" alt="" />
        </div>
        <div class="device-prop flexColumnCenter">
          <h1>{{ device.name }}</h1>
          <p>{{ device.description }}</p>
          <div class="icons">
            <img @click="showModal = true" src="comentario.png" alt="" />
            <img v-if="user.data[0].perfilFK == 2" src="deletar.png" alt="" />
          </div>
        </div>
      </div>
    </div>
    <div id="abrirModal" class="modal" v-show="showModal">
      <a href="#fechar" title="Fechar" class="fechar">x</a>
      <h2>Janela Modal</h2>
      <p>Esta é uma simples janela de modal.</p>
      <p>
        Você pode fazer qualquer coisa aqui, página de Login, pop-ups, ou
        formulários
      </p>
    </div>
  </main>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "home",
  data() {
    return {
      devices: "",
      user: this.$store.state.User,
      base_url: this.$store.state.BASE_URL,
      showModal: false,
    };
  },
  async mounted() {
    // this.idVaga = this.$route.fullPath.replace(/^\D+/g, "");

    this.$axios
      .$get(this.$store.state.BASE_URL + "/devices/?status=1")
      .then((response) => {
        this.devices = response.data;
        console.log(this.devices);
      });
  },

  created() {
    this.print();
  },
  methods: {
    print() {
      console.log("teste");
      console.log(this.user.data[0].perfilFK);
    },
    logout() {
      this.$router.push("/");
    },
  },
};
</script>

<style lang="scss">
::-webkit-scrollbar {
  display: none;
}

* {
  font-size: 19px;
}
.flexRowCenter {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.flexColumnCenter {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.main {
  width: 100vw;
  height: auto;
  min-height: 100vh;

  .modal {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: rgba(0, 0, 0, 0.8);
    z-index: 99999;
    opacity: 0;
    -webkit-transition: opacity 400ms ease-in;
    -moz-transition: opacity 400ms ease-in;
    transition: opacity 400ms ease-in;
    pointer-events: none;

    div {
      width: 400px;
      position: relative;
      margin: 10% auto;
      padding: 15px 20px;
      background: #fff;
    }

    &:target {
      opacity: 1;
      pointer-events: auto;
    }
    .fechar {
      position: absolute;
      width: 30px;
      right: -15px;
      top: -20px;
      text-align: center;
      line-height: 30px;
      margin-top: 5px;
      background: #ff4545;
      border-radius: 50%;
      font-size: 16px;
      color: #8d0000;
    }
  }

  .header {
    height: 110px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-content: center;
    justify-content: space-between;
    background-color: #cce2e2;
    padding: 1rem;

    img {
      width: 450px;
      height: 100px;
    }

    .nav-buttons {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      justify-items: center;
      width: 400px;

      .new {
        display: flex;
        flex-direction: row;
        align-content: center;
        justify-content: center;
        align-items: center;
        font-size: 26px;
        color: #35797d;
        cursor: pointer;
        &:hover {
          color: #44babc;
        }
      }

      img {
        width: 35px;
        height: 35px;
        cursor: pointer;
      }
    }
  }

  .content {
    width: 100%;
    min-height: 100vh;

    .equips {
      margin-bottom: 50px;
      padding: 6rem;
      .image {
        border: 1px solid #44babc;
        height: 400px;
        width: 60%;
        img {
          width: 100%;
          height: 100%;
        }
      }

      .device-prop {
        margin: 20px;
        h1 {
          font-size: 22px;
          margin-bottom: 5px;
          color: #b3b3b3;
        }
        p {
          margin-top: 15px;
          margin-bottom: 15px;
        }

        .icons {
          margin-top: 10px;
          display: flex;
          img {
            width: 35px;
            height: 35px;
            margin-right: 20px;

            cursor: pointer;
          }
        }
      }
    }
  }
}
</style>
