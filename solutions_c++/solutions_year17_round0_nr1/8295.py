#include <fstream>
#include <cstring>
#include <string>
#define NMAX 1010

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

char sir[NMAX];
bool sw[NMAX];

int main()
{
    //initialize
    int t, T;
    int swaps;
    int totalSwaps;
    int lg, k, i;

    cin >> T; cin.get();
    for(t = 1; t <= T; ++t){
        //clear
        swaps = 0;
        totalSwaps = 0;

        //read
        cin.getline(sir, NMAX);
        if(t == 17){
            t = 17;
        }
        lg = strlen(sir);
        for(i = lg-1; i > 0; i--)
            if(sir[i] == ' '){
                sir[i] = '\0';
                i++;
                k = sir[i]-'0';
                while(i < lg-1){
                    i++;
                    k*=10+(sir[i]-'0');
                }
                break;
            }
        lg = strlen(sir);

        //compute
        for(i = 0; i <= lg-k; i++){
            sw[i] = false;

            if(i >= k){
                if(sw[i-k] == true){
                    swaps--;
                }
            }

            if(sir[i] == '+'){
                if(swaps %2 != 0){
                    //change an + * 2*swaps from - to +
                    sw[i] = true;
                    swaps++;
                    totalSwaps++;
                }
            }
            else{ //ch == '-'
                if(swaps %2 == 0){
                    sw[i] = true;
                    swaps++;
                    totalSwaps++;
                }
            }

        }
        for(; i < lg; i++){
            if(sw[i-k] == true){
                swaps--;
            }

            if((sir[i] == '+' && swaps %2 == 1) || (sir[i] == '-' && swaps %2 == 0)){
                totalSwaps = -1;
                break;
            }
        }

        cout << "Case #" << t << ": ";
        if(totalSwaps == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << totalSwaps << '\n';
    }
    return 0;

}
