pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t devops-backend:latest backend/'
            }
        }

        stage('Test') {
            steps {
                sh 'docker images'
            }
        }
    }
}
