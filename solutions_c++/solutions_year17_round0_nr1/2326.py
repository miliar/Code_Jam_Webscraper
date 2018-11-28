#include <iostream>
#include <string>

using namespace std;

long long int algorithm (string input,unsigned int k,unsigned int min_count){
    bool complete=true;
    unsigned int first_pos;
    for (unsigned int i=0;i<input.length();i++){
        if (input.at(i)=='-'){
            first_pos=i;
            complete=false;
            break;
        }
    }
    if (complete){return min_count;}
    else {
        if (input.find('+',first_pos)==string::npos){
            if ((input.length()-first_pos)%k!=0){
                return -1;
            }
            else {return min_count+((input.length()-first_pos)/k);}
        }
        else {
            unsigned int second_pos=input.find('+',first_pos);
            if (input.find('-',second_pos)==string::npos){
                if ((second_pos-first_pos)%k!=0){
                    return -1;
                }
                else {return min_count+((second_pos-first_pos)/k);}
            }
            else {
                if (min_count%2==1){
                    for (unsigned int i=input.length()-1;i>=0;i--){
                        if (input.at(i)=='-'){
                            first_pos=i;
                            break;
                        }
                    }
                }
                if (min_count%2==0){
                    if (first_pos>input.length()-k){return -1;}
                    else {
                        for (unsigned int curr_pos=first_pos;curr_pos<first_pos+k;curr_pos++){
                            if (input.at(curr_pos)=='+'){
                                input.replace(curr_pos,1,"-");
                            }
                            else {input.replace(curr_pos,1,"+");}
                        }
                        return algorithm(input,k,min_count+1);
                    }
                }
                else {
                    if (first_pos<k-1){return -1;}
                    else {
                        int pos_temp=first_pos;
                        for (int curr_pos=pos_temp;pos_temp-curr_pos<k;curr_pos--){
                            if (input.at(curr_pos)=='+'){
                                input.replace(curr_pos,1,"-");
                            }
                            else {input.replace(curr_pos,1,"+");}
                        }
                        return algorithm(input,k,min_count+1);
                    }
                }
            }
        }
    }
}

int main()
{
    unsigned int tc_count;
    cin >> tc_count;
    for (unsigned int tc=0;tc<tc_count;tc++){
        string input;
        unsigned int k;
        cin >> input >> k;
        long long int min_count=0;
        min_count=algorithm(input,k,min_count);
        if (min_count==-1){
            cout << "Case #" << tc+1 << ": IMPOSSIBLE" << '\n';
        }
        else {
            cout << "Case #" << tc+1 << ": " << min_count << '\n';
        }
    }
    return 0;
}
