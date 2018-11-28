//
//  main.cpp
//  procon
//
//  Created by Niko@LOS on 2017/03/07.
//
//
/*
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    long x;
    cin>>x;
    unsigned int i = 1;
    unsigned int n = 0;
    while (x > 0) {
        x = x - i;
        i++;
        n++;
    }
    cout << n <<endl;
}
*/
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    
    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    
    int numCase;
    fin >> numCase;
    
    //problem solve
    for (int i = 0; i < numCase; i++)
    {
        string cake;
        unsigned int pan;
        fin >> cake;
        fin >> pan;
        unsigned long max_num = cake.size() - pan + 1;
        unsigned long ans = 0;
        for (int j = 0; j < max_num; j++){
            //int temp = strcmp(&cake[j], "+");
            if (cake[j] != '+'){
                for(unsigned int k = j; k < j + pan; k++){
                    if (cake[k] != '+') cake.replace(k, 1, "+"); else cake.replace(k, 1, "-");;
                }
                ans++;
            }
        }
        bool hantei = true;
        for(unsigned long k = max_num - 1 ; k < cake.size(); k++){
            if (cake[k] == '-') hantei = false;
        }
        if (hantei) fout << "Case #" << (i + 1) << ": " << ans << endl;
        else fout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
    }
    //problem end
    
    fin.close();
    fout.close();
    return 0;
}