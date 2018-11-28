#include<bits/stdc++.h>
using namespace std;

bool areSorted(int n)
{
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    int t;
    cin >> t;
    int tc = 0;
    while(t--){
        tc++;
        int n;
        cin >> n;
        for(int i=n; i>=0; i--){
            if(areSorted(i)){
                cout << "Case #" << tc << ": " << i << endl;
                break;
            }
        }



        //cout << "Case #" << tc << ": " << res << endl;
        //cerr << "Case #" << tc << ": " << res << endl;

    }
}
