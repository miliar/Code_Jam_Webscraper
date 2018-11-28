#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    ifstream in;
    in.open("C-small-1-attempt0.in");
    in >> t;
    ofstream out;
    out.open("result.txt");
    for(int cs=0;cs<t;cs++){
        int n,k;
        in>>n>>k;
        int a[n+2],ls[n+2],rs[n+2];
        a[0]=1;
        a[n+1]=1;
        ls[0]=0;
        rs[0]=n;
        ls[n+1]=n;
        rs[n+1]=0;
        for(int i=1;i<n+1;i++){
            a[i]=0;
            ls[i]=i-1;
            rs[i]=n-i;
        }
        while(k--){
            int c1,c2,c3;
            int flag=0;
//            cout<<n<<endl;
            for(int i=1;i<n+1;i++)
            {
//                cout<<"Hello"<<i<<"\n";
                if(a[i]==0){
                    if(flag==0){
                        c1 = min(ls[i],rs[i]);
                        c2 = max(ls[i],rs[i]);
                        c3 = i;
                        flag=1;
                    }
                    else{
                        if(c1<min(ls[i],rs[i])){
                            c1 = min(ls[i],rs[i]);
                            c2 = max(ls[i],rs[i]);
                            c3 = i;
                        }
                        else if(c1==min(ls[i],rs[i])){
                            if(c2<max(ls[i],rs[i])){
                                c2 = max(ls[i],rs[i]);
                                c3 = i;
                            }
                        }
                    }
                }
            }
//            cout<<"Hello\n";
//            cout<<c3<<endl;
            a[c3]=1;
//            cout<<"Hello\n";
            for(int j=c3-1;j>=0;j--){
                rs[j]=min(rs[j],c3-j-1);
            }
            for(int j=c3+1;j<n+2;j++){
                ls[j]=min(ls[j],j-c3-1);
            }
//            for(int i=0;i<n+2;i++)
//            {
//                cout<<a[i]<<" ";
//            }
//            cout<<endl;
//            for(int i=0;i<n+2;i++)
//            {
//                cout<<i<<" "<<ls[i]<<" "<<rs[i]<<endl;
//            }
            if(k==0){
                out<<"Case #"<<cs+1<<": "<<max(ls[c3],rs[c3])<<" "<<min(ls[c3],rs[c3])<<endl;
            }
        }
    }
    return 0;
}
