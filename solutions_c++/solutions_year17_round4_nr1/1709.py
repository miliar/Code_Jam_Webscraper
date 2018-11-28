#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        int n,p;
        scanf("%d%d",&n,&p);
        vector<int> v;
        int tmp;
        for(int i=0;i<n;i++){
        scanf("%d",&tmp);
        v.push_back(tmp);
        }
        int res=0;
        if(p==2){for(int i=0;i<n;i++){if(v[i]%2)res++;}res/=2;}
        if(p==3){
            int nb1=0;int nb2=0;
            for(int i=0;i<n;i++){if(v[i]%3==1)nb1++;if(v[i]%3==2)nb2++;}
            int gp2 = min(nb1,nb2);
            int gp3 = (max(nb1,nb2)-gp2);//the rest
            res = gp2 + (2*(gp3/3));
            if(gp3%3==2) res++;
        }
        if(p==4){}

        printf("Case #%d: %d\n",cas,n-res);


    }

    return 0;
}

