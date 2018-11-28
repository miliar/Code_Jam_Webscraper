#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
typedef unsigned int uii;
int t,n,b[6],cas,tot;
vector<string> vec[3];
string gao(int x,string a,string b) {
    string ret=a;
    --x;
    while (x) {
        ret+=b;
        ret+=a;
        --x;
    }
    return ret;
}
bool zero() {
    for (int i=0;i<6;++i)
        if (b[i])
            return false;
    return true;
}
bool check() {
    string ret="";
    if (b[1]==b[4]&&b[1]) {
        for (int i=0;i<b[1];++i)
            ret+="BO";
        b[1]=b[4]=0;
        if (zero()) {
            cout<<ret<<endl;
        } else {
            puts("IMPOSSIBLE");
        }
        return true;
    } else if (b[3]==b[0]&&b[0]) {
        for (int i=0;i<b[3];++i)
            ret+="RG";
        b[3]=b[0]=0;
        if (zero()) {
            cout<<ret<<endl;
        } else {
            puts("IMPOSSIBLE");
        }
        return true;
    } else if (b[5]==b[2]&&b[2]) {
        for (int i=0;i<b[2];++i)
            ret+="YV";
        b[5]=b[2]=0;
        if (zero()) {
            cout<<ret<<endl;
        } else {
            puts("IMPOSSIBLE");
        }
        return true;
    }
    return false;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large2.out","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        printf("Case #%d: ",cas);
        scanf("%d",&n);
        for (int j=0;j<6;++j)
            scanf("%d",&b[j]);
        if (check())
            continue;
        for (int j=0;j<3;++j)
            vec[j].clear();
        if (b[1]) {
            if (b[4]<=b[1]) {
                puts("IMPOSSIBLE");
                continue;
            } else
                b[4]-=(b[1]+1);
            vec[0].push_back(gao(b[1]+1,"B","O"));
        }
        for (int j=0;j<b[4];++j)
            vec[0].push_back(gao(1,"B","O"));
        if (b[3]) {
            if (b[0]<=b[3]) {
                puts("IMPOSSIBLE");
                continue;
            } else
                b[0]-=(b[3]+1);
            vec[1].push_back(gao(b[3]+1,"R","G"));
        }
        for (int j=0;j<b[0];++j)
            vec[1].push_back(gao(1,"R","G"));
        if (b[5]) {
            if (b[2]<=b[5]) {
                puts("IMPOSSIBLE");
                continue;
            } else
                b[2]-=(b[5]+1);
            vec[2].push_back(gao(b[5]+1,"Y","V"));
        }
        for (int j=0;j<b[2];++j)
                vec[2].push_back(gao(1,"Y","V"));
        if (vec[0].size()>vec[1].size())
            swap(vec[0],vec[1]);
        if (vec[0].size()>vec[2].size())
            swap(vec[0],vec[2]);
        if (vec[1].size()>vec[2].size())
            swap(vec[1],vec[2]);
        tot=0;
        for (int i=0;i<3;++i)
            tot+=vec[i].size();
        if ((int)vec[2].size()*2>tot) {
            puts("IMPOSSIBLE");
            continue;
        }
        while (vec[2].size())
            if (vec[0].size()+vec[1].size()>vec[2].size()) {
                cout<<vec[2][vec[2].size()-1];
                cout<<vec[0][vec[0].size()-1];
                cout<<vec[1][vec[1].size()-1];
                vec[0].resize(vec[0].size()-1);
                vec[1].resize(vec[1].size()-1);
                vec[2].resize(vec[2].size()-1);
            } else {
                cout<<vec[2][vec[2].size()-1];
                vec[2].resize(vec[2].size()-1);
                if (vec[0].size()) {
                    cout<<vec[0][vec[0].size()-1];
                    vec[0].resize(vec[0].size()-1);
                } else {
                    cout<<vec[1][vec[1].size()-1];
                    vec[1].resize(vec[1].size()-1);
                }
            }
        cout<<endl;
    }
    return 0;
}
