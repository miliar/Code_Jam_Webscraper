 #include <bits/stdc++.h>
using namespace std;

int t, N, R, O, Y, G, B, V;
bool vis[100];
queue<char> q;

void Add2(char st, char en)
{
    char prv=st, tmp;
    while(R+B+Y>=0){
        //printf("%d,%d,%d  ", R, B, Y);
        if(prv=='R'){
            //printf("R,%d,%d  ", B, Y);
            if(B==0 && Y==0){
                if(prv==en){
                    tmp=q.back();
                    if(tmp=='R')
                        R++;
                    if(tmp=='B')
                        B++;
                    if(tmp=='Y')
                        Y++;
                    q.push('X');
                }
                return;
            }
            else if(B==Y){
                if( en=='B')
                    q.push('B'), B--;
                else
                    q.push('Y'), Y--;
            }
            else if(B>Y){
                q.push('B'), B--;
            }
            else if(Y>B){
                q.push('Y'), Y--;
            }
        }
        else if(prv=='B'){
            //printf("B,%d,%d  ", R, Y);
            if(R==0 && Y==0){
                if(prv==en){
                    tmp=q.back();
                    if(tmp=='R')
                        R++;
                    if(tmp=='B')
                        B++;
                    if(tmp=='Y')
                        Y++;
                    q.push('X');
                }
                return;
            }
            else if(R==Y){
                if( en=='R')
                    q.push('R'), R--;
                else
                    q.push('Y'), Y--;
            }
            else if(R>Y){
                q.push('R'), R--;
            }
            else if(Y>R){
                q.push('Y'), Y--;
            }
        }
        else if(prv=='Y'){
            //printf("Y,%d,%d  ", R, B);
            if(R==0 && B==0){
                if(prv==en){
                    tmp=q.back();
                    if(tmp=='R')
                        R++;
                    if(tmp=='B')
                        B++;
                    if(tmp=='Y')
                        Y++;
                    q.push('X');
                }
                return;
            }
            else if(R==B){
                if(en=='R')
                    q.push('R'), R--;
                else
                    q.push('B'), B--;
            }
            else if(R>B){
                q.push('R'), R--;
            }
            else if(B>R){
                q.push('B'), B--;
            }
        }
        prv=q.back();
    }
}

int main()
{
   freopen("r.txt","r",stdin);
   freopen("output.txt", "w", stdout);
   cin>>t;
   for(int u=0;u<t;u++){
    while(!q.empty())
      q.pop();
    memset(vis, 0, sizeof 0);

    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
    printf("Case #%d: ", u+1);
    if(V+Y==N && V==Y){
        for(int i=0;i<V;i++)
           printf("YV");
        printf("\n");
        continue;
    }
    if(O+B==N && O==B){
        for(int i=0;i<O;i++)
           printf("BO");
        printf("\n");
        continue;
    }
    if(G+R==N && G==R){
        for(int i=0;i<G;i++)
           printf("GR");
        printf("\n");
        continue;
    }
    if((O+1>B && O!=0) || (V!=0 && V+1>Y) || (G!=0 && G+1>R)){
        printf("IMPOSSIBLE\n");
        continue;
    }
    vis['O']=(O>0), vis['V']=(V>0), vis['G']=(G>0);

    if(vis['O']+vis['V']+vis['G']==3){
        B-=(O+1), Y-=(V+1), R-=(G+1);
        for(int i=0;i<O;i++)
            q.push('B'),q.push('O');
        q.push('B');
        Add2('B', 'Y');

        for(int i=0;i<V;i++)
            q.push('Y'),q.push('V');
        q.push('Y');
        Add2('Y', 'R');

        for(int i=0;i<G;i++)
            q.push('R'), q.push('G');
        q.push('R');
        Add2('R', 'B');
    }

    else if(vis['O']+vis['V']+vis['G']==2){
        if(vis['O']+vis['V']==2){
            B-=(O+1), Y-=(V+1);
            for(int i=0;i<O;i++)
                q.push('B'),q.push('O');
            q.push('B');
            Add2('B', 'Y');

            for(int i=0;i<V;i++)
                q.push('Y'),q.push('V');
            q.push('Y');
            Add2('Y', 'B');
        }
        else if(vis['V']+vis['G']==2){
            Y-=(V+1), R-=(G+1);
            for(int i=0;i<V;i++)
                q.push('Y'),q.push('V');
            q.push('Y');
            Add2('Y', 'R');

            for(int i=0;i<G;i++)
                q.push('R'), q.push('G');
            q.push('R');
            Add2('R', 'Y');
        }
        else if(vis['O']+vis['G']==2){
            B-=(O+1), R-=(G+1);
           for(int i=0;i<O;i++)
                q.push('B'),q.push('O');
            q.push('B');
           Add2('B', 'R');

            for(int i=0;i<G;i++)
                q.push('R'), q.push('G');
            q.push('R');
            Add2('R', 'B');
        }
    }

    else if(vis['O']+vis['V']+vis['G']==1){
        if(O>0){
            B-=(O+1);
            for(int i=0;i<O;i++)
                q.push('B'),q.push('O');
            q.push('B');
            Add2('B', 'B');
        }
        if(V>0){
            Y-=(V+1);
            for(int i=0;i<V;i++)
                q.push('Y'),q.push('V');
            q.push('Y');
            Add2('Y', 'Y');
        }
        if(G>0){
            R-=(G+1);
            for(int i=0;i<G;i++)
                q.push('R'), q.push('G');
            q.push('R');
            Add2('R', 'R');
        }
    }

    else if(vis['O']+vis['V']+vis['G']==0){
        //printf("HERE");
        int M=max(B, max(R , Y));
        if(M==B)
            B--, q.push('B'), Add2('B', 'B');
        else if(M==R)
            R--, q.push('R'), Add2('R', 'R');
        else if(M==Y)
            Y--, q.push('Y'), Add2('Y', 'Y');
    }
    //("HERE");
    if(B!=0 || R!=0 || Y!=0){
        printf("IMPOSSIBLE\n");
        continue;
    }
    string pr;
    while(!q.empty()){
      pr+=q.front(), q.pop();
    }
    int ln=pr.size();
    for(int i=0;i<ln;i++){
        if(i==ln-1)
            printf("%c",pr[i]);
        else{
            if(pr[i+1]=='X')
                i++;
            else
                printf("%c",pr[i]);
        }
    }
    printf("\n");
   }


    return 0;
}
