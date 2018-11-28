#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
using namespace std;

int main(){
    int t;
    //freopen("A-large.in","r",stdin);
    cin >> t;
    int tt=t;
    while(t--){
        string s;
        cin >> s;
        int k;
        cin >>k;
        queue<int>q;
        int i=0;
        int cnt=0;
        for(i=0;i<s.size()-k+1;i++){
          //  cout << "runing for " << i << endl;
            if(!q.empty()){
                if(i-q.front()+1>k){
                    q.pop();
                }
            }
            if((s[i]=='-'&&(q.size()%2==0)) || (s[i]=='+'&&(q.size()%2==1))){
                q.push(i);
                cnt++;
            //    cout << "pusing "<< i<< " cnt " << cnt << endl;
            }
        }
        //cout << cnt << endl;
        bool imp=false;
        while(i<s.size()){
            if(!q.empty()){
                if(i-q.front()+1>k){
                    q.pop();
                }
            }
            if(s[i]=='+'&&(q.size()%2==1)){
               imp=true;
               break;
            }
            else if(s[i]=='-'&&(q.size()%2==0)){
               imp=true;
               break;
            }
            i++;
        }
        if(imp){
            cout << "Case #"<<tt-t<<": IMPOSSIBLE"<< endl;
        }
        else {
            cout << "Case #"<<tt-t<<": "<<cnt<< endl;
        }

    }
    return 0;
}
