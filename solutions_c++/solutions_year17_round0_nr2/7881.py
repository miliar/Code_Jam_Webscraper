#include<bits/stdc++.h>
#include <string>
#include <stdio.h>
#include <iostream>   // std::cout
#include <fstream>
#define CIN ios::sync_with_stdio(false) ,cin.tie(0);

using namespace std;


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
    while(getline(file, test)) /// file name
    {
        i++;
        string num = test;

        for(int j = 1 ; j < num.length(); j++)
        {
            char prev = num[j-1];
            char current = num[j];
            if(current < prev)
            {
                int index = j;
                while(num[--index] == prev)
                {}
                index++;
                num[index]--;
                if(index == 0 && num[index] == '0')
                {
                    // make all the opt 9999s
                    for(int k = 0 ; k < num.length()-1 ; k++)
                    {
                        num[k] = '9';
                    }
                    num = num.substr(0,num.size()-1);
                }
                else
                {
                    for(int k = index+1 ; k < num.length() ; k++)
                    {
                        num[k] = '9';
                    }

                    //make rest 9999s
                }


                break;

            }

        }
        outfile << "Case #" << i << ": " << num<< endl;
        if( i == test_cases) break;
    }

    outfile.close();
    file.close();
    return 0;
}

/*

freopen("A-small-attempt0.in", "r", stdin);
freopen("oneA.txt", "w", stdout);


*/
