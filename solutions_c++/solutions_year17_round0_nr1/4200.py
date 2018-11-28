#include <iostream>
#include <string>
#include <bitset>

using namespace std;

void calc(string str, int n)
{
    int l = str.length();
    if ( l == 0) {
        cout << 0 << endl;
        return;
    } 
    bitset<2048> b;
    int count = 0;

    for(int j = 0; j < l ; j++){
        if (str[j] == '-') {
            b.flip(j);
        }

        if (b.test(j)) {
            //cout << "test " << b << ":" << j << " t" << endl;
            for(int i = 0; i < n ; i++){
                b.flip(j+ i);
            }
            count ++;
        }
    }
    
        for(int i = 0; i < n ; i++){
             if (b.test(l+i)){
                cout <<  "IMPOSSIBLE" << endl;
                return;
            }
        }        
    
        cout << count << endl;
}

int main()
{
    int T, i, n;
    string str;
    cin >> T;
    i = T;
    while (i-- > 0)
    {
        cin >> str >> n;
        cout << "Case #" << T - i << ": " ;
        calc(str, n);
    }
}