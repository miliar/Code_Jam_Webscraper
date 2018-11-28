//
//  codejam.cpp
//  codejam
//
//  Created by Zimu Wang on 4/8/17.
//
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;
int main(){
    ifstream fin ("B-large.in");
    ofstream fout ("B-large.out");
    int cases;
    fin >> cases;
    string input;

    string ans;
    for (int i=0;i<cases;i++){
        
        fin >> input;
        //cout <<input<<endl;
        string test = "";
        int position = 0;
        ans = "";
        while (position < input.length() - 1 && input[position] <= input[position+1]){
            position ++ ;
        }
        //cout << position << endl;
        if (position == input.length() -1 ){
            fout << "Case #" << i+1 << ": " << input << endl;
        }
        else{
            while (position >= 1 && input[position] == input[position - 1]){
                position --;
            }
            //cout << position<<endl;
            if (position == 0 && input[position]=='1'){
                for (int j=0;j<input.length() - 1;j++){
                    ans += '9';
                }
                //cout << "HERE"<<endl;
                fout << "Case #" << i+1 << ": " << ans << endl;
            }
            else{
                for (int j = 0 ; j < position;j++){
                    ans += input[j];
                }
                ans += input[position] - 1;
                
                int helper = input.length() - ans.length();
                for (int j=0;j<helper;j++){
                    ans += '9';
                }
                
                fout << "Case #" << i+1 << ": " << ans << endl;
            }
        
        }
    }
    //fout.close();
}
