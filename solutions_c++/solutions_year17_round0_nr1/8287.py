#include <iostream>
#include <string>
#include <map>
#include <queue>
using namespace std;

string flippart(string s,int pos, int count){
    string temp = s;
    for(int i = pos;i<pos+count;i++){
        if(temp[i] == '-') temp[i] = '+';
        else temp[i] = '-';
    }
    return temp;
}

int getFlips(string s, int k){
    map<string,bool> vs;
    queue<string> q;
    map<string,int> depth;
    string final_state;
    for(int i = 0;i<s.size();i++){
        final_state.push_back('+');
    }
    //cout<<"final string "<<final_state<<endl;
    q.push(s);
    depth[s] = 0;
    while(!q.empty()){
        string state = q.front();
        q.pop();
        
        //cout<<"current state "<<state<<endl;
        //cout<<"depth "<<depth[state]<<endl;
        if(state == final_state){
            return depth[state]; 
        }
        vs[state] = true;
        for (int i = 0;i < state.size() - k + 1; i++){
            string next_state = flippart(state,i,k);
            if(!vs[next_state]){
                q.push(next_state);
                //cout<<next_state<<endl;
                depth[next_state] = depth[state]+1;
                //cout<<depth[next_state]<<endl;
            }
        }
    }
    return -1;
}

int main(){
    int t;
    cin>>t;
    string s;
    int k;
    int i = 1;
    while(t--){
        cin>> s >> k;
        int flips = getFlips(s,k);
        if(flips == -1){
            cout<<"Case #"<<i++<<": "<<"IMPOSSIBLE"<<endl;
        }else{
            cout<<"Case #"<<i++<<": "<<flips<<endl;
        }
    }
}
