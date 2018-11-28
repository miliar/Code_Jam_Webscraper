#include <bits/stdc++.h>
#define prev fjioweajiof
#define x1 fjweoifakewop
#define y1 zfewfjwieofajoi
using namespace std;

const int nmax = 100010;
const int inf = 1e9;

int t, n, m;
string s[30];

int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

cin >> t;
int tests=0;
while (t--){
tests++;
    cin >> n >> m;
    for (int i=0; i<n; i++) cin >> s[i];


            for(int j = 0; j<n; j++)
                {
                    for(int k = 0; k<m; k++)
                    {
                        if(s[j][k]!='?')
                        {
                            for(int p = k + 1; p<m; p++)
                                if(s[j][p] == '?')
                                    s[j][p] = s[j][k];
                                else
                                    break;
                            for(int p = k - 1; p>=0; p--)
                                if(s[j][p] == '?')
                                    s[j][p] = s[j][k];
                                else
                                    break;
                        }
                    }
                }
                for(int j = 0; j<(n - 1); j++)
                {
                    for(int kpop = 0; kpop<m; kpop++)
                        if(s[j][kpop] != '?' && s[j + 1][kpop] == '?')
                            s[j + 1][kpop] = s[j][kpop];
                }
                for(int j = n - 1; j>0; j--)
                {
                    for(int kpop = 0; kpop<m; kpop++)
                        if(s[j][kpop] != '?' && s[j - 1][kpop] == '?')
                            s[j - 1][kpop] = s[j][kpop];
                }
                cout<<"Case #"<<tests<<":"<<endl;
                for(int i = 0; i<n; i++)
                {
                    cout << s[i] << endl;
                }


}


return 0;
}

