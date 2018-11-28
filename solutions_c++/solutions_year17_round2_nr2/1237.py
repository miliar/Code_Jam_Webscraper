#include <iostream>
#include<vector>
#include<algorithm>
#include<cstdio>

using namespace std;
char tab[128];
int exp[128];
char f(char t)
{
    if(t=='B') return 'O';
    if(t=='R') return 'G';
    if(t=='Y') return 'V';
}
int main()
{
    freopen("data.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        int N,R,O,Y,G,B,V;
        scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
        int x=B-O;
        int y=R-G;
        int z=Y-V;

        if(B==O&&(R+Y+G+V)==0){
            printf("Case #%d: ",kase);
            while(B--){
                printf("BO");
            }
            printf("\n");
            continue;
        }
        if(R==G&&(R+G)==N){
            printf("Case #%d: ",kase);
            while(R--){
                printf("RG");
            }
            printf("\n");
            continue;
        }

        if(Y==V&&(Y+V)==N){
            printf("Case #%d: ",kase);
            while(Y--){
                printf("YV");
            }
            printf("\n");
            continue;
        }

        if(x<0||y<0||z<0){
            printf("Case #%d: IMPOSSIBLE\n",kase);
            continue;
        }
        tab['x']='B'; exp['x']=O;
        tab['y']='R'; exp['y']=G;
        tab['z']='Y'; exp['z']=V;
        if(x<y){
            swap(x,y);swap(B,R);swap(O,G); swap(tab['x'],tab['y']); swap(exp['x'],exp['y']);
        }
        if(y<z){
            swap(y,z);swap(R,Y);swap(G,V); swap(tab['z'],tab['y']); swap(exp['z'],exp['y']);
        }
        if(x<y){
            swap(x,y);swap(B,R);swap(O,G); swap(tab['x'],tab['y']); swap(exp['x'],exp['y']);
        }
        //cout<<x<<" "<<y<<" "<<z<<endl;
        //cout<<tab['x']<<" "<<tab['y']<<" "<<tab['z']<<endl;
        if(x>y+z){
            printf("Case #%d: IMPOSSIBLE\n",kase);
            continue;
        }
        int a=y,b=y+z-x;
        string ans;
        for(int i=0;i<x;i++){
            ans.push_back(tab['x']);
            while(exp['x']>0){
                --exp['x'];
                ans.push_back(f(tab['x']));
                ans.push_back(tab['x']);
            }
            if(b>0){
                b--;
                ans.push_back(tab['z']);
            }
            if(a>0){
                a--;
                ans.push_back(tab['y']);

                    while(exp['y']>0){
                    --exp['y'];
                    ans.push_back(f(tab['y']));
                    ans.push_back(tab['y']);
                }
            }
            else {
                ans.push_back(tab['z']);

                    while(exp['z']>0){
                    --exp['z'];
                    ans.push_back(f(tab['z']));
                    ans.push_back(tab['z']);
                }
            }
        }
        printf("Case #%d: %s\n",kase,ans.c_str());
    }
    return 0;
}
