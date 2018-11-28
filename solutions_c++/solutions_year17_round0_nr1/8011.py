#include<iostream>  // includes cin to read from stdin and cout to write to stdout
#include<stdio.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int k,sum,n,flag;
char a[1005];

/*int x(int a,int b){
    for(int i=2;i*i<=a;i++)
        if(a%i==0&&b%i==0)return 1;
    return 0;
}*/

int main() {
    freopen("problemA-sample.in","r",stdin);
    freopen("problemA-sample.out","w",stdout);
    //freopen("pancakes.in","r",stdin);
    //freopen("pancakes.out","w",stdout);
    int i,j,s,t=0,max=0,maxlo=0,m=0,m1,mlo,ms,f;
    char b;
    scanf("%d\n",&n);
    
    for(j=1;j<=n;j++){
        f=0;
        sum=0;
        for(s=1;;s++){
            scanf("%c",&b);
            if(int(b)!=32)a[s]=b;
            else break;
            if(int(b)==43)t++;
        }
        scanf("%d\n",&k);

        s--;
        //printf("s=%d\n",s);
        /*for(int x=1; x<=s; x++) {
            printf("%d,", a[x]);
        }

        printf(" count = %d\n", k);*/

        if(k>s){
            cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        if(k==1){
            cout<<"Case #"<<j<<": "<<t<<endl;
            continue;
        }
        //flag=0;
        while(1){
            flag=1;
            ms=0;
            max=0;
            //mlo=0;
            for(i=1;i<=s;i++){
                if(int(a[i])==45){
                    if(flag==1){m1=i;flag=0;}
                    while(int(a[i+m])==45)m++;
                    ms++;
                    mlo=i;
                    //flag=1;
                    i=i+m;

                    //printf("m=%d\n",m);
                    //printf("i=%d\n",i);
                }
                else m=0;
                if(m>max){
                    max=m;
                    maxlo=mlo;
                    m=0;
                }
            }
            //for(i=1;i<=s;i++)printf("%c",a[i]);
            //printf("\n");
            //printf("%d %d\n",ms,maxlo);
            if(ms==0)break;
            
            if((ms==1&&max<k)){
                cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
                f=1;
                break;
            }
            else {
                for(i=m1;i<m1+k;i++){
                    if(int(a[i])==43)a[i]='-';
                    else a[i]='+';
                }
                //flag=1;
                
                
            }
            sum++;
        }
        if(!f)cout<<"Case #"<<j<<": "<<sum<<endl;
    }
    
    
    
    /*for (int i = 1; i <= t; ++i) {
        cin >> n >> m;  // read n and then m.

        cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }*/
    return 0;
}