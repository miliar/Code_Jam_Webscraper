#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)

stack<string> generate(int x,int yz, string tx, string tyz) {
    if (x == 0) return stack<string>();
    int l = x-yz-1;
    stack<string> ans;
    string tmp = tx;
    FOR(i,yz) tmp+= tyz+tx;
    ans.push(tmp);
    FOR(i,l) ans.push(tx);
    return ans;
}

string generate_one(int k, string x) {
    string ans = "";
    FOR(i,k) ans+=x;
    return ans;
}

void solve() {
    int n,r,ry,y,yb,b,rb;
    scanf("%d%d%d%d%d%d%d",&n,&r,&ry,&y,&yb,&b,&rb);
    
    if (r+yb ==n && r==yb) {
        printf("%s\n",generate_one(r,"RG").c_str());
        return;
    }
    if (y+rb == n && y==rb) {
        printf("%s\n",generate_one(y,"YV").c_str());
        return;
    }
    if (b+ry == n && b==ry) {
        printf("%s\n",generate_one(b,"BO").c_str());
        return;
    }
    
    // check edge case, only 2 colors
    
    int xx = r - yb;
    int yy = y - rb;
    int zz = b - ry;
    
    if ((xx < 1 && yb > 0)  || (yy < 1 && rb > 0) || (zz < 1 && ry > 0)) puts("IMPOSSIBLE");
    else {
        if(xx+yy >= zz && xx+zz>=y && yy+zz>=xx) {
            
            auto tx = generate(r,yb,"R","(YB)"); // G
            auto ty = generate(y,rb,"Y","(RB)"); // V
            auto tz = generate(b,ry,"B","(RY)"); // O
            
            auto cur = make_pair(tz.size(), 'B');
            if (tx.size() > 0) cur = make_pair(tx.size(), 'R');
            if (ty.size() > 0) cur = make_pair(ty.size(), 'Y');
            
            string ans = "";
            
            while(1) {
                
                //printf("%s %d %d %d\n",ans.c_str(), tx.size(), ty.size(), tz.size());
                
                if (cur.first == 0) break;
                
                auto tmp = cur;
                
                switch (cur.second) {
                    
                    case 'R': ans+=tx.top(); tx.pop(); tmp = max(make_pair(ty.size(), 'Y'), make_pair(tz.size(), 'B')); break;
                    case 'Y': ans+=ty.top(); ty.pop(); tmp = max(make_pair(tx.size(), 'R'), make_pair(tz.size(), 'B')); break;
                    case 'B': ans+=tz.top(); tz.pop(); tmp = max(make_pair(tx.size(), 'R'), make_pair(ty.size(), 'Y')); break;
                    
                }
                
                cur = tmp;
            }
            
            printf("%s\n",ans.c_str());
            
            
            // generate solution
            
        }
        else puts("IMPOSSIBLE");
    }
}


int main(void) {
    int t;
    scanf("%d\n",&t);
    FOR(i,t) {
        printf("Case #%d: ", i+1);
        solve();
    }
    
}
