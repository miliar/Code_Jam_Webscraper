#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

pair<int,int> vv(int n,int g){
//    printf("%d %d",n,g);
    int l = (10*n)/(11*g);
    if((10*n)%(11*g)!=0)l++;
    int r = (10*n)/(9*g);
    return make_pair(l,r);
}


int main(){
    FILE *in=fopen("input.txt", "r");
    FILE *out=fopen("output.txt","w");

    int tt;
    fscanf(in,"%d",&tt);

    int make[100];


    for(int tc=1;tc<=tt;tc++){
        int ans = 0;
        vector<int> Q[100];
        int v[105][105] = {0,};

        int n,p;
        fscanf(in,"%d %d",&n,&p);
        for(int i=0;i<n;i++){
            fscanf(in,"%d",&make[i]);
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++){
                int num;
                fscanf(in,"%d",&num);
                pair<int,int> rest = vv(num,make[i]);
                if(rest.second<rest.first)continue;
                //printf("%d\n",num);

                Q[i].push_back(num);
            }
            std::sort(Q[i].begin(),Q[i].end());
        }

        for(int i=0;i<n*p;i++){

            int flag = 0;
            int maxValue = 0;
            int x,y;
            for(int j=0;j<n;j++){
                for(int k=0;k<Q[j].size();k++){
                    pair<int,int> rest = vv(Q[j][k],make[j]);
                    if(v[j][k] == 0){
                        if(rest.first>maxValue){
                            x = j;
                            y = k;
                            maxValue = rest.first;
                        }
                        break;
                    }
                }
            }
            //printf("%d %d %d\n",x,y,ans);
            vector<int> g;

            for(int j=0;j<n;j++){
                for(int k=0;k<Q[j].size();k++){
                    pair<int,int> rest = vv(Q[j][k],make[j]);

                    if(rest.second<maxValue){
                        v[j][k] = 1;
                    }
                    if(v[j][k] == 0){
                        if(rest.second>=maxValue){
                            g.push_back(k);
                            break;
                        }
                    }
                }
            }
            if(g.size() != n){
                v[x][y] = 1;
            }
            else{
                ans ++;
                for(int j=0;j<n;j++){
                    v[j][g[j]]=1;
                }
            }
        }
        fprintf(out,"Case #%d: %d\n",tc,ans);
    }
}
