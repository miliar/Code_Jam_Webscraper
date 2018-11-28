#include<bits/stdc++.h>
using namespace std;
/*
void subtract(int a[],int n){

    int b[25];
    int i;
    for( i = 0; i < n - 1; i++)
        b[i] = 0;
    b[i] = 1;

    for(int k = n - 1 ; k >= 0 ; k--){

        int diff = a[k] - b[k];

        if(diff < 0){
            diff += 10;
            a[k - 1]--;
        }
        a[k] = diff;
    }
}

bool check(int a[],int n){

    for(int i = 1 ; i < n ; i++){
        if(a[i - 1] > a[i])
            return false;
    }

    return true;
}
*/
int main(){

   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);

    int t;
    cin>>t;

    int cases = 1;

        while(t--){

            string s;
            cin>>s;

            int a[25];
            int n = s.size();
            for(int i = 0 ; i < s.size() ; i++){
                    a[i] = s[i] - '0';
            }
            /*
            while(!check(a,n)){
                subtract(a,n);
            }*/

            bool flag = false;
            cout<<"Case #"<<cases++<<": ";

            for(int i = 0 ; i < n - 1 ; i++){
                if(a[i + 1] < a[i]){
                    a[i]--;
                for(int j = i + 1 ; j < n ; j++)
                        a[j] = 9;
                    if(i >= 1)
                        i -= 2;
                    else
                        i = 0;
                }
            }

            for(int i = 0 ; i < n ; i++){
                    if(a[i] == 0){
                        if(flag)
                            cout<<a[i];
                    }
                    if(a[i] != 0){
                        flag = true;
                        cout<<a[i];
                    }
            }
            cout<<endl;
        }


    return 0;
}
