#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


struct stall{

    int index;
    int y; // max(Ls,Rs)
    int z; // min(Ls,Rs)

};


int main(){

    int T;
    int N;
    int K;
    cin>>T;
    for (int i=0;i<T;i++){

        cin>>N;
        cin>>K;
        if(N==K){
            cout<<"Case #"<<i+1<<": "<< 0<<" "<<0<<endl;
        }
        else{
            vector<bool> stalls(N+2,false);
        stalls[0]=stalls[N+1]=true;

        for(int k=1;k<=K;k++){  //for every person
            stall chosenStall;
            for(int j=1;j<N+1;j++){
                if(!stalls[j]){
                    chosenStall.index=j;
                    int leftcounter=0;
                    int rightcounter=0;
                    for(int l=j-1;l>=0;l--){
                        if(stalls[l])
                            break;
                        else
                            leftcounter++;
                    }
                    for(int r=j+1;r<N+2;r++){
                        if(stalls[r])
                            break;
                        else
                            rightcounter++;
                    }
                    chosenStall.y=max(leftcounter,rightcounter);
                    chosenStall.z=min(leftcounter,rightcounter);
                    break;
                }

        }

        for(int j=chosenStall.index+1;j<N+1;j++){
                if(!stalls[j]){
                    stall thisStall;
                    thisStall.index=j;
                    int leftcounter=0;
                    int rightcounter=0;
                    for(int l=j-1;l>=0;l--){
                        if(stalls[l])
                            break;
                        else
                            leftcounter++;
                    }
                    for(int r=j+1;r<N+2;r++){
                        if(stalls[r])
                            break;
                        else
                            rightcounter++;
                    }
                    thisStall.y=max(leftcounter,rightcounter);
                    thisStall.z=min(leftcounter,rightcounter);
                    if(thisStall.z>chosenStall.z){
                        chosenStall=thisStall;
                    }
                    else if(thisStall.z==chosenStall.z){
                        if(thisStall.y>chosenStall.y){
                            chosenStall=thisStall;
                        }
                    }
                }
        }

        stalls[chosenStall.index]=true; //mark the chosen stall as occupied

        if (k==K){//last person
            cout<<"Case #"<<i+1<<": "<< chosenStall.y<<" "<<chosenStall.z<<endl;
        }
    }
}
}

    return 0;
}
