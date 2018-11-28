#include <fstream>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int v[20];

int main()
{
    long long n, cn;
    int T;
    int z, i, j;
    cin >> T;
    for(int t = 1; t <=T; t++){
        cin >> n; cn = n;
        z = 0;
        while(cn != 0){
            z++;
            v[z] = cn%10;
            cn/=10;
        }
        v[z+1] = -1;
        for(i = z-1; i > 0; i--){
            if(v[i] < v[i+1]){
                //error
                int index = i+1;
                while(index < z){
                    if(v[index] == 0) index++;
                    else if(v[index] -1 < v[index+1]) index++;
                    else break;
                }

                v[index]--;
                if(index == z && v[index] == 0) z--;
                for(j = index-1; j > 0; j--)
                    v[j] = 9;
                break;


            }
        }
        cout << "Case #" << t << ": ";
        for(i = z; i > 0; i--)
            cout << v[i];
        cout << '\n';
    }
    return 0;
}
