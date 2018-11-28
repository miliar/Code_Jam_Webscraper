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
 
 //google jam problem a
 
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
 
 */


//google jam problem b

#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int ctoi(char c){
    switch(c){
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
        default : return -1;
    }
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    
    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    
    int numCase;
    fin >> numCase;
    
    //problem solve
    for (int i = 0; i < numCase; i++)
    {
        string target;
        fin >> target;
        unsigned long max_num = target.size();
        vector<int > ans;
        for(int j = 0; j < max_num; j++) ans.push_back(0);
        int now = ctoi(target[max_num-1]);
        if (max_num == 1) fout << "Case #" << (i + 1) << ": " << target <<endl ;
        else{
        for (long j = max_num - 1; j > 0; j--){
            int next = ctoi(target[j - 1]);
            
            
            ans[j] = now;
            
            if (now < next){
                for(unsigned long k = j; k < max_num; k++){
                    ans[k] = 9;
                }
                next--;
            }
            ans[j-1] = next;
            int temp = next;
            now = temp;
        }
        unsigned long j = 0;
        while (ans[j] == 0) {
            j++;
        }
        fout << "Case #" << (i + 1) << ": " ;
        for(unsigned long k = j; k < max_num; k++) fout << ans[k];
        fout << endl;
        }
    }
    //problem end
    
    fin.close();
    fout.close();
    return 0;
}