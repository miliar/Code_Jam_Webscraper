#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
        long long n, temp, count=1, rem;
        cin >> n;
        temp=n;
        while(temp=temp/10){
            count++;
        }
        //cout << count;
        long long digits[count];
        temp=count;
        while(n>0){
            rem=n%10;
            digits[temp-1]=rem;
            temp--;
            n=n/10;
        }
        int x,y,z;
        x=count-1;
        y=count-2;
        while(y>=0){
           if(digits[y]<=digits[x]){
                x--;
                y--;
            } else {
                digits[y]--;
                for(z=x;z<count;z++){
                    digits[z]=9;
                }
            }
        }
        cout << "Case #" << i+1 << ": ";
        for(int j=0; j<count; j++){
            if(digits[j] != 0){
                cout << digits[j];
            }
        }
        cout << endl;
    }
    fclose (stdin);
    fclose (stdout);
    return 0;
}
