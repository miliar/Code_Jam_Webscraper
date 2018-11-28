#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int cakeState(vector<string> &, vector<char> &);
bool fillCake(vector<string> &, vector<char> &);
void printCake(vector<string> &);

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        int R, C;
        cin >> R >> C;
        vector<char> symbols;
        vector<string> cake;
        cake.resize(R);
        for(int j = 0; j < R; ++j)
        {
            cin >> cake[j];
            for(unsigned int l = 0; l < cake[j].size(); ++l)
            {
                if(cake[j][l] == '?')
                    continue;
                int skip = 0;
                for(unsigned int k = 0; k < symbols.size() && !skip; ++k)
                {
                    if(cake[j][l] == symbols[k])
                    {
                        skip = 1;
                    }
                }
                if(skip == 0)
                    symbols.push_back(cake[j][l]);
            }
        }
        //cout << symbols.size() << '\n';
        //cout << "Cake:\n";
        //printCake(cake);
        //cout << "Symbols: ";
        //for(unsigned int j = 0; j < symbols.size(); ++j) cout << symbols[j] << ' ';
        //cout << "\n\n";
        fillCake(cake, symbols);
        cout << "Case #" << i << ":\n";
        for(unsigned int j = 0; j < cake.size(); ++j)
            cout << cake[j] << '\n';
    }
    return 0;
}

int cakeState(vector<string> &cake, vector<char> &symbols)
{
    int result = 1;
    for(unsigned int j = 0; j < cake.size(); ++j)
        for(unsigned int k = 0; k < cake[j].size(); ++k)
            if(cake[j][k] == '?')
                result = 0;
    for(unsigned int i = 0; i < symbols.size(); ++i)
    {
        unsigned int tlr = cake.size(), tlc = cake[0].size(), brr = 0, brc = 0;
        for(unsigned int j = 0; j < cake.size(); ++j)
        {
            for(unsigned int k = 0; k < cake[j].size(); ++k)
            {
                if(symbols[i] == cake[j][k])
                {
                    //cout << "Symbol: " << symbols[i] << ", " << j << ", " << k << '\n';
                    if(j < tlr)
                        tlr = j;
                    if(k < tlc)
                        tlc = k;
                    if(j > brr)
                        brr = j;
                    if(k > brc)
                        brc = k;
                    //cout << tlr << ' ' << brr << ',' << tlc << ' ' << brc << '\n';
                }
            }
        }
        //cout << tlr << ' ' << brr << ',' << tlc << ' ' << brc << '\n';
        for(unsigned int j = tlr; j <= brr; ++j)
        {
            for(unsigned int k = tlc; k <= brc; ++k)
            {
                //cout << "Failed at: " << symbols[i] << ", " << j << ", " << k << "\n\n";
                if(cake[j][k] != '?' && cake[j][k] != symbols[i])
                    return -1;
            }
        }
    }
    return result;
}

bool fillCake(vector<string> &cake, vector<char> &symbols)
{
    int result = cakeState(cake, symbols);
    //cout << "\nfillCake: " << result << "\n";
    //printCake(cake);
    if(result > 0)
        return true;
    if(result < 0)
        return false;
    //cout << "ONWARD!\n";
    for(unsigned int i = 0; i < symbols.size(); ++i)
        for(unsigned int j = 0; j < cake.size(); ++j)
            for(unsigned int k = 0; k < cake[j].size(); ++k)
            {
                if(cake[j][k] == '?')
                {
                    //cout << "Curious...\n";
                    cake[j][k] = symbols[i];
                    if(fillCake(cake, symbols))
                        return true;
                    cake[j][k] = '?';
                }
            }
    return false;
}

void printCake(vector<string> &cake)
{
    for(unsigned int j = 0; j < cake.size(); ++j)
            cout << cake[j] << '\n';
}
