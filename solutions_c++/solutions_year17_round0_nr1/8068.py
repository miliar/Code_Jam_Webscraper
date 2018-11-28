#include <iostream>

using namespace std;

char rev(char a){
    return a=='+'?'-':'+';
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int i = 1; i<=t; i++){
        string txt;
        int k;
        cin >> txt;
        cin >> k;
        int res = 0;
        int n = txt.size();
        for(int f = 0; f<=n-k; f++)
        {
            if(txt[f] == '-'){
                res++;
                for(int j = 0; j<k; j++)
                    txt[f+j] = rev(txt[f+j]);
            }
        }
        bool posible = true;
        for(int f = n-k; f<n; f++){
            if(txt[f] == '-')
                posible = false;
        }
        if(!posible){
            cout << "Case #" << i <<": IMPOSSIBLE\n";
        }else{
            cout << "Case #" << i <<": " << res <<"\n";
        }
    }
    return 0;
}
