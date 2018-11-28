#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    string lel;
    getline(cin,lel);
    for(int t = 0; t < T; t++)
    {

        string num;
        getline(cin,num);
                int mark = num.size();
        for(int i = num.size()-1; i>0;i--){
            if(num[i]<num[i-1]){
                mark = i;
                num[i-1]--;
            }
        }
    cout << "Case #" << t+1 << ": ";
    if(num[0] != '0')
    {
        cout << num[0];
    }
    for(int i = 1;i<num.size();i++)
    {
        if(i>=mark)
        cout << 9;
        else cout << num[i];
    }
    cout << endl;
    }



    return 0;
}
