#include<bits/stdc++.h>
using namespace std;

struct P{
    int L;
    int R;

    bool operator < (const P &other) const
    {
        int diff1 = R-L;
        int diff2 = other.R - other.L;

        return (diff2 > diff1);
    }

};



int main(){
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int N,T,K;

    scanf("%d",&T);


    for(int k = 0; k < T; k++){

        priority_queue <P> Q;

        scanf("%d %d",&N,&K);

        N+=2;


        int L = 2, R = N-1;

        Q.push({L,R});
        //cout << "Case #" << k+1 << ": ";
        printf("Case #%d: ",k+1);
        for(int l = 1; l <= K; l++){
            P temp = Q.top();
            Q.pop();
            //cout << temp.L << " " << temp.R << endl;

            int S = (temp.L + temp.R) / 2;

            if(l == K){
                //cout << S << " " << temp.L << " "<< temp.R << endl;
                //cout << max(S-temp.L,temp.R-S) << " " << min(S-temp.L,temp.R-S) << endl;
                printf("%d %d\n",max(S-temp.L,temp.R-S),min(S-temp.L,temp.R-S));
                break;

            }

            Q.push({temp.L,S-1});
            Q.push({S+1,temp.R});



        }



    }

}
