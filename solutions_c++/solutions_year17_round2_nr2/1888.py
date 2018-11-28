#include<bits\stdc++.h>
using namespace std;
void __main(int test){
    int N,R,O,Y,G,B,V;
    cin>>N>>R>>O>>Y>>G>>B>>V;
    if(R>N/2||Y>N/2||B>N/2){
        cout<<"IMPOSSIBLE";
        return;
    }
    int fN,sN,tN;
    char fC,sC,tC;
    if(R>=Y&&Y>=B){
        fN=R; sN=Y; tN=B;
        fC='R'; sC='Y'; tC='B';
    }else if(R>=B&&B>=Y){
        fN=R; sN=B; tN=Y;
        fC='R'; sC='B'; tC='Y';
    }else if(B>=R&&R>=Y){
        fN=B; sN=R; tN=Y;
        fC='B'; sC='R'; tC='Y';
    }else if(B>=Y&&Y>=R){
        fN=B; sN=Y; tN=R;
        fC='B'; sC='Y'; tC='R';
    }else if(Y>=R&&R>=B){
        fN=Y; sN=R; tN=B;
        fC='Y'; sC='R'; tC='B';
    }else if(Y>=B&&B>=R){
        fN=Y; sN=B; tN=R;
        fC='Y'; sC='B'; tC='R';
    }

    char arr[3*N];
    for(int i=0;i<3*N;i++)arr[i]=' ';
    int start=0;
    for(int i=start,j=fN;i<3*fN&&j>0;j--,i+=3){
        while(arr[i]!=' ')i++;
        arr[i]=fC;
    }
    start=1;
    int i,j;
    for(i=start,j=sN;i<3*fN&&j>0;j--,i+=3){
        while(arr[i]!=' ')i++;
        arr[i]=sC;
    }
    i%=3*fN;
    for(j=tN;i<3*fN&&j>0;j--,i=(i+3)%(3*fN)){
        while(arr[i]!=' ')i=(i+1)%(3*fN);
        arr[i]=tC;
    }

    for(int i=0;i<3*N;i++)
        if(arr[i]!=' ')
            cout<<arr[i];
}
int main()
{
    int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        cout<<"Case #"<<t<<": ";
        __main(t);
        cout<<endl;
    }
    return 0;
}

