#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> PII;
typedef pair<PII,PII> PIIII;
typedef pair<PIIII,int> PIIIII;

queue<PIIIII> q;
map<PIIII,bool> mem;
int t,tes,h1,a1,h2,a2,b,d,ans;

int main() {
    scanf("%d",&t);
    for (tes=1 ; tes<=t ; tes++) {
        scanf("%d%d%d%d%d%d",&h1,&a1,&h2,&a2,&b,&d);
        mem.clear();
        while (!q.empty()) q.pop();
        
        mem[PIIII(PII(h1,a1),PII(h2,a2))] = true;
        q.push(PIIIII(PIIII(PII(h1,a1),PII(h2,a2)),0));
        
        ans = 1000000;
        while (!q.empty()) {
            PIIIII tmp = q.front();
            q.pop();
            
            int h11 = tmp.first.first.first;
            int a11 = tmp.first.first.second;
            int h22 = tmp.first.second.first;
            int a22 = tmp.first.second.second;
            int x = tmp.second;
            
            //printf("%d %d %d %d %d\n",h11,a11,h22,a22,x);
            
            if (h22 == 0 || x == 1000000) {
                ans = x;
                break;
            }
            
            {
                int h11_new = h11;
                int h22_new = h22;
                int a11_new = a11;
                int a22_new = a22;
                
                h22_new = max(0,h22 - a11);
                if (h22_new > 0) h11_new = max(0,h11 - a22);
                a11_new = a11;
                a22_new = a22;
                
                if (h11 > 0 && !mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))]) {
                    mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))] = true;
                    q.push(PIIIII(PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new)),x+1));
                }
            }
            
            {
                int h11_new = h11;
                int h22_new = h22;
                int a11_new = a11;
                int a22_new = a22;
                
                a11_new = a11 + b;
                if (h22_new > 0) h11_new = max(0,h11 - a22);
                
                if (h11 > 0 && !mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))]) {
                    mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))] = true;
                    q.push(PIIIII(PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new)),x+1));
                }
            }
            
            {
                int h11_new = h11;
                int h22_new = h22;
                int a11_new = a11;
                int a22_new = a22;
                
                if (h22_new > 0) h11_new = max(0,h1 - a22);
                
                if (h11 > 0 && !mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))]) {
                    mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))] = true;
                    q.push(PIIIII(PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new)),x+1));
                }
            }
            
            {
                int h11_new = h11;
                int h22_new = h22;
                int a11_new = a11;
                int a22_new = a22;
                
                a22_new = max(0,a22 - d);
                if (h22_new > 0) h11_new = max(0,h11 - a22_new);
                
                if (h11 > 0 && !mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))]) {
                    mem[PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new))] = true;
                    q.push(PIIIII(PIIII(PII(h11_new,a11_new),PII(h22_new,a22_new)),x+1));
                }
            }
        }
        
        printf("Case #%d: ",tes);
        if (ans == 1000000) printf("IMPOSSIBLE\n"); else printf("%d\n",ans);
    }
}
