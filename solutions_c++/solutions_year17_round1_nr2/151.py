// need x, have y
// x*serve*0.9 <= y <= x*serve*1.1
// LS: serve <= y/0.9/x
// RS: serve >= y/1.1/x


#include <stdio.h>
#include <vector>
#include <algorithm>


int t1,t2;
int n,p;

int needed[64];

std::vector<int> ing[64];
int ans;

bool good;
int serve;

int docase()
{
    scanf("%d%d",&n,&p);
    for (int i=0; i<n; i++) {
        scanf("%d",needed+i);
        ing[i].clear();
    }
    for (int i=0; i<n; i++) {
        for (int j=0; j<p; j++) {
            scanf("%d",&t1);
            ing[i].push_back(t1);
        }
        std::sort(ing[i].begin(),ing[i].end());
    }
    ans=0;
    while (1) {
        // keep getting the largest servings possible
        serve=1000000000;
        for (int i=0; i<n; i++) {
            if (ing[i].empty()) return ans;
            if (serve>(ing[i].back()*10/9/needed[i])) {
                serve=(ing[i].back()*10/9/needed[i]);
            }
        }
        good=1;
        //printf("serve %d\n",serve);
        for (int i=0; i<n; i++) {
            // check if serve is too low
            while ((serve*needed[i]*11)<10*ing[i].back()) {
                //printf("failed %d\n",i);
                good=0;
                ing[i].pop_back();
                if (ing[i].empty()) return ans;
            }
        }
        if (good) {
            ans++;
            for (int i=0; i<n; i++) {
                ing[i].pop_back();
            }
        }
    }
}

int t;
int main()
{
    #ifdef NOT_DMOJ
    freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif // NOT_DMOJ
    scanf("%d",&t);
    for (int i=1; i<=t; i++) printf("Case #%d: %d\n",i,docase());
}
