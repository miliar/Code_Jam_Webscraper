#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define rep(a,b) for(int a = 0; a < (int)b; a++)

string s;

int main(){
    //freopen("b2.in", "r", stdin);
    //freopen("b2.out", "w", stdout);
    int T;
    cin>>T;

    int breakPosition;

    rep(t, T){
        cout<<"Case #"<<t+1<<": ";
        cin>>s;
        breakPosition = -1;
        rep(i, s.size()){
            if(!i){
                continue;
            }

            if(s[i] < s[i - 1]){
                breakPosition = i;
                //todo: solve the thing
                s[i - 1]--;
                i--;
                while(i and s[i] < s[i - 1]){
                    breakPosition--;
                    s[i - 1]--;
                    i--;
                }

                //todo: print the solution

                rep(j, s.size()){
                    if(j >= breakPosition){
                        cout<<'9';
                    }else if(s[j] != '0'){
                        cout<<s[j];
                    }
                }
                cout<<endl;

                break;
            }

        }


        if(breakPosition == -1){//The break position did not change,so the number is already tidy
            cout<<s<<endl;
        }
    }
    return 0;
}

