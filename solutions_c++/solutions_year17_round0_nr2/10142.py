#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<sstream>
#include<stdlib.h>
#include<math.h>
using namespace std;

long long denomGen(int n){
    cout<< "\npo: "<<pow(10,n)<<"n = "<<n<<endl;;
    long long op=10;
    for(int i = 2;i<=n;i++){
        op*=10;
    }


    return op;
}


int main(){
    //*****************************
    string output_string="";
    ofstream outfile;
    outfile.open("tidy_output.txt");
    ostringstream convert;
    string case_no,answer;
    //*****************************
    ifstream infile;
    infile.open("input.in");

    int T;
    infile >> T;
    cout<<T<<endl;
    int tt=1;
    long long number;
    string temp_number;
    int digit,prev;
    int mod_index;
    bool not_clear;
    int mod_den_size;
    long long denom;
    for(int tt=1;tt<=T;tt++){
        mod_index = 0;
        infile>>number;
        convert << number;
        temp_number = convert.str();
        convert.str("");
        convert.clear();
        //cout<<endl<<temp_number;
        not_clear = false;
        int input_num_size = temp_number.size();
        int siz = temp_number.size();
        long long my_half;
        for(int i=0;i<input_num_size-1;i++){
                //cout<<"Comparing :"<<temp_number.at(i)-'0'<<"   "<<temp_number.at(i+1)-'0'<<" i ====="<<i<<endl;
            if(temp_number.at(i)-'0' == temp_number.at(i+1)-'0'){
                    //cout<<"cond 1"<<endl;
                   // if(temp_number.at(i)>'1'){
                        mod_index = i;
                   // }
                continue;
            }else if((temp_number.at(i)-'0') < (temp_number.at(i+1)-'0')){
                mod_index = i+1;
            //cout<<"cond 2"<<endl;
            }
            else if(temp_number.at(i)-'0' > temp_number.at(i+1)-'0'){ // mod you stay there
                    mod_index++;
           // cout<<"cond 3"<<endl;
                //get mod din value
                not_clear = true;
                //length of mod din
                mod_den_size = abs(mod_index - siz);
                //generate denominator
                denom = denomGen(mod_den_size);
                //cout<<"II-============"<<temp_number.at(i);
                //cout<<"denom : "<<denom<<" mod siz : "<<mod_den_size<<"from position : "<<(i)<<"model index : "<<mod_index<<endl;
//                if(((i-1)>=0)&&(temp_number.at(i)!='1')&&(temp_number.at(i-1)==temp_number.at(i))){
//                    my_half = number % denom ;
//                    //cout<<endl<<"my half "<<my_half<<endl;
//                    long long denom_10 = (denom/10);
//                   // cout<<endl<<"my denm_10 :  "<<denom_10<<endl;
//                    my_half = my_half - (my_half - (my_half-((my_half-denom_10) + 1)));
//                   // cout<<endl<<"my half after processing : "<<my_half<<endl;
//                    number = number / denom;
//                   // cout<<endl<<"my number  after cutting down extra : "<<my_half<<endl;
//                    number = (number * denom_10);
//                   // cout<<endl<<"add zeros to number :  "<<number<<endl;
//                    number+=my_half;
//                    //cout<<endl<<"after adding result :  "<<number<<endl;
//
//                }else{
                    number = number - (number % denom + 1);
                //cout<<"\nans : "<<number<<endl;
                //}
                break;


            }

        }
                    convert << tt;
            case_no = convert.str();
            convert.str("");
            convert.clear();
        //cout<<""<<number<<endl;
            convert << number;
            answer = convert.str();
            convert.str("");
            convert.clear();
            output_string += "Case #"+case_no+": "+answer+"\n";


    }
        outfile<<output_string;
    outfile.close();
    infile.close();



    return 0;
}

