#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Output.out","w",stdout);
    int t, k, move_count, plus_count, flag;
    cin >> t;
    for (int loop=1;loop<=t;loop++){
        move_count=0;
        flag=0;
        string s;
        cin >> s >> k;
        //cout << k<< " "<<s.size();
        while(1){
            move_count++;
            plus_count=0;
            for (int i=0;i<s.size();i++){
                if (s[i]=='+'){ plus_count++; }
                else{
                    if (s.size()-i >= k){
                        for (int j=i;j<i+k;j++){
                            if (s[j]=='+') s[j]='-';
                            else s[j]='+';
                        }
                    }
                    else{
                        flag=1;
                    }
                    break;
                }
            }
            //cout << "move-"<<move_count<<" "<<s<<endl;
            if (plus_count == s.size() || flag==1) break;
        }
        if (flag==1){
            cout << "Case #"<< loop <<": IMPOSSIBLE"<<endl;
        }
        else{
            cout << "Case #"<<loop<<": "<<move_count-1<<endl;
        }
    }
    return 0;
}
