#include<iostream>
#include<cstdio>
using namespace std;
/*bool tidy(long long int n, int pre)
{
    if (n==0) return true;
    if( n%10 <= pre ) {
        return tidy(n/10, n%10);
    }
    else return false;
}*/
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cs=0;
    long long n, a;
    cin>>t;
    while(t--) {
        cin>>n;
        a = n;
        int tmp[20], num[20], cnt=0, x=0;
        for(int i=0; a!=0 ; i++) {
            tmp[i] = a%10;
            a /= 10;
            cnt++;
        }
        for(int i=0; i<cnt; i++) num[i] = tmp[cnt-i-1];
        //for(int i=0; i<cnt; i++) cout<<num[i];
        //cout<<endl;
        for(int i=cnt-1; i>=0; i--) {
            if(i==0) {
                break;
            }
            if( num[i-1]>num[i] || num[i]==0 ) {
                num[i] = 9;
                for(int j=i; j<cnt; j++) num[j] = 9;
                num[i-1] = num[i-1] - 1;
            }
        }
        cout<<"Case #"<<++cs<<": ";
        while(num[x]==0) { x++; }
        for(int i=x; i<cnt; i++) cout<<num[i];
        cout<<endl;
    }
    return 0;
}
