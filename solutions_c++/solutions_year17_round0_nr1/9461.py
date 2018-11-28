#include <bits/stdc++.h>

using namespace std;

string s;
int nt,k,allflips;


void flip(int p) {
    allflips++;
    for(int i = 0; i < k; i++)
        if(s[p+i] == '-') s[p+i] = '+';
        else s[p+i] = '-';
}

int main()
{
//    freopen("input.txt","r",stdin);
    //freopen("al.in","r",stdin);
    //freopen("al.out","w",stdout);

    cin >> nt;
    for(int t = 1; t <= nt; t++) {
        cin >> s >> k;
        allflips = 0;
        for(int i = 0; i < s.length()-k+1; i++) {
            if(s[i] == '-') flip(i);
            //cout<<s<<endl;
        }

        for(int i = s.length()-k+1; i < s.length(); i++)
            if(s[i] == '-') allflips = -1;

        cout<<"Case #"<<t<<": ";
        if(allflips == -1) cout<<"IMPOSSIBLE"<<endl;
        else cout<<allflips<<endl;
    }

    return 0;
}
