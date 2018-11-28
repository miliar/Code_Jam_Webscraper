#include<bits/stdc++.h>
#include <string>
#include <stdio.h>
#include <iostream>   // std::cout
#include <fstream>
#define CIN ios::sync_with_stdio(false) ,cin.tie(0);

using namespace std;

vector<string> split( const char *str, char c )
{
    vector<string> result;

    do
    {
        const char *begin = str;

        while(*str != c && *str)
            str++;

        result.push_back(string(begin, str));
    }
    while (0 != *str++);

    return result;
}



int main()
{
    CIN;
    ifstream file("input_file.txt");
    string test;
    ofstream outfile;
    outfile.open("outputFile.txt");
    getline(file, test);
    int test_cases = atoi( test.c_str() );
    int i = 0 ;
    while(getline(file, test )) /// file name
    {

        i++;
        const char *char_token = test.c_str();
        vector <string> vect = split(char_token, ' ');
        int count_flips = 0;
        int k = atoi( vect[1].c_str());
        test = vect[0];
        bool imp = false;



        for(int i = 0 ; i < test.length()  ; i++)
        {
            if(test[i] == '-' && (test.length() - i < k))
            {
                imp = true;
                break;
            }
            else if(test[i] == '-')
            {
                count_flips++;
                test[i] = '+';
                for(int j = i+1 ; j < k+i ; j++ )
                {
                    if(test[j] == '-')
                    {
                        test[j] = '+';
                    }
                    else
                    {
                        test[j] = '-';
                    }
                }


            }

        }

        if(imp)
        {
            outfile << "Case #" << i << ": IMPOSSIBLE"<< endl;

        }else{
            outfile << "Case #" << i << ": " << count_flips<< endl;
        }
        if( i == test_cases) break;
    }

    outfile.close();
    file.close();
    return 0;
}
