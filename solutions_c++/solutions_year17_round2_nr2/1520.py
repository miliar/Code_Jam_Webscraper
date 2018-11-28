#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007

bool comp(string& rem, int r, int b, int y) {
    vector<pair<int, char> > chrs;
    chrs.pb(mp(r, 'R'));
    chrs.pb(mp(b, 'B'));
    chrs.pb(mp(y, 'Y'));
    sort(chrs.rbegin(), chrs.rend());
    int n = rem.sz;
    if(chrs[0].ff>(n+1)/2) {
        cout<<"IMPOSSIBLE"<<endl;
        return false;
    }
    for(int i = 0;i<n;i+=2) {
        if(rem[i]!='-')
            continue;
        for(int j = 0;j<3;j++) {
            if(chrs[j].ff>0) {
                rem[i] = chrs[j].ss;
                chrs[j].ff--;
                break;
            }
        }
    }
    for(int i = 1;i<n;i+=2) {
        if(rem[i]!='-')
            continue;
        for(int j = 0;j<3;j++) {
            if(chrs[j].ff>0) {
                rem[i] = chrs[j].ss;
                chrs[j].ff--;
                break;
            }
        }
    }
    return true;
}
bool match(char a, char b) {
    if(a == b) {
        return true;
    }
    if(a == 'O' && b!= 'B') {
        return true;
    }
    if(a == 'G' && b!= 'R') {
        return true;
    }
    if(a == 'V' && b!= 'Y') {
        return true;
    }
    if(b == 'O' && a!= 'B') {
        return true;
    }
    if(b == 'G' && a!= 'R') {
        return true;
    }
    if(b == 'V' && a!= 'Y') {
        return true;
    }
    return false;
}
bool valid(string& ans) {
    int n = ans.ln;
    bool found = true;
    fore(i,0,n-1) {
        found = found & (!match(ans[i], ans[i+1]));
    }
    found = found & (!match(ans[0], ans[n-1]));
    return found;
}
int tot(int a, int b, int c, int d) {
    return a+b+c+d;
}
int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
	    printf("Case #%d: ",z+1);
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		int sec = 0;
		if(o>0)
            sec++;
        if(g>0)
            sec++;
        if(v>0)
            sec++;
        if(o==b && tot(r,g,v,y)==0) {
            fore(i,0,b) {
                cout<<"OB";
            }
            cout<<endl;
            continue;
        }
        if(r==g && tot(o,b,v,y)==0) {
            fore(i,0,g) {
                cout<<"RG";
            }
            cout<<endl;
            continue;
        }
        if(v==y && tot(r,g,o,b)==0) {
            fore(i,0,y) {
                cout<<"VY";
            }
            cout<<endl;
            continue;
        }
        if((o>0 && b<=o) || (g>0 && r<=g) || (v>0 && v<=y) ) {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        if(o>0)
            b-=o+1;
        if(g>0)
            r-=g+1;
        if(v>0)
            y-=v+1;
        int lft = b+r+y;
        string rem(b+r+y, '-');
        if(sec == 1) {
            if(o>0) {
                if(b<=(lft-1)/2) {
                    for(int i = 1;i<lft-1;i+=2) {
                        if(b<=0) {
                            break;
                        }
                        rem[i] = 'B';
                        b--;
                    }
                }
                else {
                    cout<<"IMPOSSIBLE"<<endl;
                    continue;
                }
            }
            else if(g>0) {
                if(r<=(lft-1)/2) {
                    for(int i = 1;i<lft-1;i+=2) {
                        if(r<=0) {
                            break;
                        }
                        rem[i] = 'R';
                        r--;
                    }
                }
                else {
                    cout<<"IMPOSSIBLE"<<endl;
                    continue;
                }
            }
            else if(v>0) {
                if(y<=(lft-1)/2) {
                    for(int i = 1;i<lft;i+=2) {
                        if(y<=0) {
                            break;
                        }
                        rem[i] = 'Y';
                        y--;
                    }
                }
                else {
                    cout<<"IMPOSSIBLE"<<endl;
                    continue;
                }
            }
        }
        if(!comp(rem, r, b, y)) {
            continue;
        }
        string rest = "GOV";
        bool found = false;
        do {
            string ans = "";
            for(int i = 0;i<rest.ln;i++) {
                if(rest[i] == 'G') {
                    fore(i,0,g) {
                        ans+="RG";
                    }
                    if(g>0) {
                        ans+='R';
                    }
                }
                else if(rest[i] == 'O') {
                    fore(i,0,o) {
                        ans+="BO";
                    }
                    if(o>0) {
                        ans+='O';
                    }
                }
                else if(rest[i] == 'V') {
                    fore(i,0,v) {
                        ans+="YV";
                    }
                    if(v>0) {
                        ans+='Y';
                    }
                }
            }
            ans = rem+ans;
            if(valid(ans)) {
                found = true;
                cout<<ans<<endl;
                break;
            }
        }while(next_permutation(all(rest)));
        if(!found) {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
	}
	return 0;
}
