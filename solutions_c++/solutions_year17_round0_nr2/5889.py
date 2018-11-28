#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char s[20];
int a[20];
ll num;

//bool check(int num)
//{
//    int bit[20], len = 0;
//    while(num){
//        bit[++len] = num%10;
//        num /= 10;
//    }
//    for(int i=len-1; i>= 0; i--){
//        if(bit[i] < bit[i+1]) return false;
//    }
//    return true;
//}

int main()
{
#ifndef ONLINE_JUDGE
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
#endif // ONLINE_JUDGE
    int t, cas=0;
    cin>>t;
    while(cas++ < t)
    {
        printf("Case #%d: ",cas);
        scanf("%s", s);
        num = 0;
        int n = strlen(s);
        for(int i=0;i<n;i++) a[i] = s[i] - '0', num = a[i] + num*10;// printf("%d",a[i]);
        //cout<<endl;

        int len=1;
        while(len < n && a[len] >= a[len-1]) len++;
        //cout<<len<<"fdsfsdf"<<endl;
        if(len == n || n == 1) printf("%s\n", s);
        else {
            int id = len-1;
            while(id >= 0 && a[id] == a[len-1]) id--;
            //cout<<cas<<"dfsdf"<<len<<" "<<id<<endl;
            if(id == -1){
                if(a[0] == 1) {
                    for(int i=0;i<n-1;i++) printf("9");
                    puts("");
                }
                else {
                    printf("%d", a[len-1]-1);
                    for(int i=1;i<n;i++) printf("%d",9);
                    puts("");
                }
            }
            else {
                for(int i=0;i<=id;i++) printf("%d",a[i]);
                printf("%d",a[len-1]-1);
                for(int i=id+2;i<n;i++) printf("%d",9);
                puts("");
            }
        }
//        while(!check(num)){
//            num --;
//        }
//        cout<<num<<endl;
    }
    return 0;
}
