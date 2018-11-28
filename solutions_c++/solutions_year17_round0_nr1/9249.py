#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    int t=1;
    while (t<=T){
        string s;
        int k,cnt=0;
        cin >> s >> k;
        int z = s.size();
        for (int i=z-1; i>=k-1; i--){
            if (s[i]=='-'){
                int d=k;
                int j=i;
                while(d) {
                    if(s[j]=='+')
                        s[j]='-';
                    else if (s[j]=='-')
                        s[j]='+';
                    j--;
                    d--;
                }
                cnt++;
            }
        }
        int f=0;
        for (int i=0; i<z; i++){
            if(s[i]=='+')
                f=1;
            else{
                f=0;
                break;
            }
        }
        if (f)
            cout << "Case #" << t << ": " << cnt << endl;
        else
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        t++;
    }
    return 0;
}
