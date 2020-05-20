node{
    
    stage("Git Clone"){
        git credentialsId: '571e0fd7-2841-4c22-ada6-92cf2febc352',branch: '10.0', url: 'https://github.com/maherjaballi/odoo.git'
    }
    
    stage("Build"){
        
       echo "*-*-*-*-*-*stage build*-*-*-*-*-*"
    }
    
    stage("Build Docker Image"){
        
        sh "docker build -t mjaballi/odoo-test  ."
    }
    
    stage("Docker Push"){
        withCredentials([string(credentialsId: 'DOCKER_HUB_CRED', variable: 'DOCKER_HUB_CRED')]) {
    // some block
             sh "docker login -u mjaballi -p ${DOCKER_HUB_CRED}"
            }
        sh "docker push mjaballi/odoo-test"
       
    }
    
    stage("Deploy"){
		echo "*-*-*-*-*-*stage deploy*-*-*-*-*-*"
        
           }
}
