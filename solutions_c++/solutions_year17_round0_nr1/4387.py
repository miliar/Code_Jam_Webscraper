#include <fstream>
#include <cstring>

using namespace std;

int t, j, sum, possible, ls, k;

int v[1002];

char s[1002];

int main()
{
    ifstream in ("infile.txt");
    ofstream out("outfile.txt");
    in>>t;
    j = 1;
    while(j <= t){
        in.get();
        in.get(s, 1002, ' ');
        in>>k;
        ls = strlen(s);
        sum = 0;
        possible = 1;
        for(int i = 0; i <= ls - k; ++i){
            if(i >= k)
                sum -= v[i - k];
            if ((s[i] == '-' && sum % 2 == 0) || (s[i] == '+' && sum % 2 == 1))
                v[i] = 1;
            else v[i] = 0;
            sum += v[i];
        }
        for(int i = ls - k + 1; i < ls; ++i){
            v[i] = 0;
            if(i >= k) sum -= v[i - k];
            if((sum % 2 == 0 && s[i] == '-') || (sum % 2 == 1 && s[i] == '+'))
                possible = 0;
        }
        out<<"Case #"<<j<<": ";
        if(possible){
            sum = 0;
            for(int i = 0; i < ls; ++i) sum += v[i];
            out<<sum;
        }
        else out<<"IMPOSSIBLE";
        out<<"\n";
        j++;
    }
    return 0;
}
