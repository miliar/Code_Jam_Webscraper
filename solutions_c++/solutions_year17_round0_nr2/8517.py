#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<string>
using namespace std;

typedef long long in;

int main(){
    in test;
    cin >> test;
    for(in t=0;t<test;t++){
        cout << "Case #" << t+1 << ": ";
        string s;
        cin >> s;
        vector<int> d(s.size());
        for(int i=0;i<s.size();i++){
            d[i]=s[i]-'0';
        }
        bool flag=0;
        for(int i=0;i<d.size()-1;i++){
            if(d[i]>d[i+1]){
                flag=1;
                if(d[i]!=1){
                    if(i!=0&&d[i-1]==d[i]){
                        cout << d[0]-1;

                    for(int j=1;j<d.size();j++)
                        cout << "9";
                    cout << endl;
                    }

                    else{
                        for(int j=0;j<i;j++)
                            cout << d[j];
                        cout << d[i]-1;
                        for(int j=i+1;j<d.size();j++)
                            cout << "9";
                        cout << endl;
                    }
                }
                else{
                    for(int j=0;j<d.size()-1;j++)
                        cout << "9";
                    cout << endl;
                }
                break;
            }
        }
        if(!flag)
            cout << s << endl;
    }
    return 0;
}
