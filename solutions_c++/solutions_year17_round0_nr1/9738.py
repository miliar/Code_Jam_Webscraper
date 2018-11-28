#include <iostream>

using namespace std;

bool isAllSunnyUp(string S){
    for(unsigned int i=0; i<S.length(); i++){
        if(S[i]=='-'){
            return false;
        }
    }
    return true;
}
int flipPanCakes(string S,int K,string history){
    //cout<< S<<endl;
    //cout << "History:" << history<<endl;
    history +=" "+S;
    if(isAllSunnyUp(S)){//base case
        return 0;
    }
    int index=S.find('-');
    if(index+K>S.length()){
        index = S.length()-K;
    }
    for(int i=0;i<K;i++){
        //flip pen cakes
        if(S[index+i]=='-'){
            S[index+i]='+';
        }else{
            S[index+i]='-';
        }
    }
    if(history.find(S)!=std::string::npos){//sequence seen before
        return -1;
    }
    int contains = history.find(S);
    //cout <<"Contains:"<< contains<<endl;
    int flips = flipPanCakes(S,K,history);
    if(flips <0){//Impossible
        return -1;
    }else{//possible
        return flips+1;
    }
}

int main()
{
    string S="";
    int K=0;
    int T=0;
    int flips =0;
    cin >>T;
    for(int i=1; i<=T; i++){
        cin >> S;
        cin >> K;
        //cout << "================"<<endl;
        flips = flipPanCakes(S,K,"");
        if(flips<0){
            cout << "Case #" << i << ": IMPOSSIBLE" <<endl;
        }else{
            cout << "Case #" << i << ": " << flips <<endl;
        }
    }
    return 0;
}
