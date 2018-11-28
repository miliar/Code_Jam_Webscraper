#include <bits/stdc++.h>
#define pb push_back
#define ll long long

using namespace std;

string n="";

long long toInt(string s)
{
    long long r = 0;
    for(int i=0;i<(int)s.size();i++)
        r = r * 10 + s[i] - '0';
    return r;
}

int verif(int pos){
    bool test=false;
    while (true){
        if (pos){
            if(n[pos-1]>n[pos]){
                    test=true;
                    pos--;
                    n[pos]--;
            }
            else
                    return pos;
        }
        else
        return pos;
    }
}
int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int j=1;j<=t;j++){
        cin >> n;
        for(int i=0;n[i+1];i++){
                if (n[i]>n[i+1]){
                    n[i]--;
                    i=verif(i);
                    for(int j=i+1;n[j];j++)
                        n[j]='9';
                        break;
                }
        }
        cout <<"Case #"<<j<<": " << toInt(n) << endl;
    }
}
