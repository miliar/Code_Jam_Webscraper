#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define rep(a,b) for(int a = 0; a < (int)b; a++)

vi tree;

void update(int idx){
    idx++;
    while (idx < tree.size()){
        //cout<<"update to "<<idx<<endl;
        tree[idx] ++;
        idx += (idx & -idx);
    }
}

int read(int idx){
    idx++;
    int sum = 0;
    while (idx > 0){
            //cout<<"read "<<endl;
        sum += tree[idx];
        idx -= (idx & -idx);
    }
    return sum % 2;
}

int main(){
    //freopen("a.in", "r", stdin);
    //freopen("a2.out", "w", stdout);
    int T, k, ans;
    cin>>T;
    string s;

    rep(t, T){
        cout<<"Case #"<<t+1<<": ";
        ans = 0;
        cin>>s>>k;

        //cout<<s<<" "<<k<<endl;

        tree = vi(s.size() + 5, 0);
        rep(i, tree.size()){
            //cout<<tree[i]<<(i == tree.size() - 1 ? "\n" : " ");
        }

        bool success = true;

        int totalChanges = 0;
        rep(i, s.size()){
            //cout<<"Total changes to do in "<<i<<" are "<<totalChanges<<endl;
            if(totalChanges & 1){
                //cout<<"Changing..."<<endl;
                s[i] = s[i] == '-' ? '+' : '-';
            }

            if(s[i] == '-'){
                if(i + k - 1 >= s.size()){//The change will affect elements outside our string
                        //so we have failed here
                    //cout<<s<<endl;
                    success = false;
                    break;
                }else{
                    s[i] = '+';
                    totalChanges ++;
                    tree[i + k - 1]++;
                    ans++;
                }
            }

            if(tree[i]){
                totalChanges--;
            }
        }

        if(success){
            cout<<ans<<endl;
        }else{
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}

