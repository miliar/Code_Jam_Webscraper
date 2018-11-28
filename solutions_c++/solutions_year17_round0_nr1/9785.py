#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;

string stringFilp(string input_str,int start,int K){
    int s_k = abs(start + (K-1));
    for(;start<=s_k;start++){
        if(input_str.at(start)=='+'){
            input_str.replace(start,1,"-");
        }else{
            input_str.replace(start,1,"+");
        }
    }
    return input_str;
}
char stringCheck(string input_str,int K){
    //cout<<input_str;
    int siz = input_str.size();
    string::iterator  it = input_str.begin();

    int neCount = 0;
    int poCount = 0;

    for(;it != input_str.end();it++){
        if(*it == '+'){
            poCount++;
        }else{
            neCount++;
        }

    }
    if(poCount == K){
        return '+';
    }else if(neCount == K){
        return '-';
    }else{
        return '*';
    }

}

int main(){
    //*****************************
    string output_string="";
    ofstream outfile;
    outfile.open("cake_output.txt");
    ostringstream convert;
    string case_no,answer;
    //*****************************
    int T;
    char op;
    cin>>T;
    string input_string;
    int tt=1;
    int K;
    int siz;
    int lock_index ;
    int flips ;
    bool not_possible;
    //cout<<"Test case : " << T<<endl;
    for(int tt=1;tt<=T;tt++){
        flips = 0;
        lock_index = -1;
        //input
        cin>>input_string;
        cin>>K;
        //cout<<endl<<"input : "<<input_string<< " K = "<<K;
        siz = input_string.size();
        not_possible = false;


        //cout<<"Test : "<<stringFilp("++++++++----------",0,5);
        //process
        for(int i=0;i<=(siz-K);i++){
           // cout<<"hell\n";
            string tmp_string;

            op = stringCheck(input_string.substr(i,K),K);
            //cout<<endl<<op<<endl;
            if(op == '-'){
               // cout<<"Message : "<<"All were - i = "<<i<<endl;
                input_string = stringFilp(input_string,i,K);
                flips++;

                i+=K-1;

                lock_index = i;
            }else if(op == '+'){
                i+=K-1;
                cout<<"i = "<<i<<" "<<(siz-K);
                lock_index = i;
                //cout<<"Message : "<<"All were + i = "<<i<<endl;
            }else{
                //cout<<"Message : "<<"third condition i = "<<i<<endl;
                if(i==(siz-K)){ //last record and if
                    //cout<<"Impossible "<<endl;
                   not_possible = true;
                    break;
                }
                if(input_string.at(i)=='+'){
                    //cout<<": "<<"At i = "<<i<<"it is +"<<endl;
                    lock_index = i;
                    continue;
                }
                if(input_string.at(i)=='+'){
                    //cout<<": "<<"At i = "<<i<<"it is +"<<endl;
                    lock_index = i;
                    continue;
                }
//                if(i+(K-1) >= siz){//not possible
//                    cout<<"Not possible "<<endl;
//                    //break;
//                }
                //flip the k elements and check for lock elements
                input_string = stringFilp(input_string,i,K);
                //cout<<"After flip : from  "<<i<<" to : "<<i+K-1<<" "<<input_string<<endl;
                //check for impossible case
                flips++;
                i--;
                /*tmp_string = stringFilp(input_string,i,K);

                int strt = abs(i - (K-1));
                int en = i;
                if(strt < 0){
                    strt = 0;
                }
                if(strt < lock_index){
                    strt = lock_index + 1;
                }
                int en_strt = (en-strt);
                //check left
                op = stringCheck(tmp_string.substr(strt,en_strt+1),en_strt);
                if(op== '+'){
                    lock_index = i;
                }else if(op== '-'){
                    if(en_strt == K ){
                        tmp_string = stringFilp(tmp_string,strt,K);
                        lock_index = en;
                    }
                }*/
//                //******************************************
//                //check right
//                 strt = i;
//                 en = i+(K-1);
//                if(en >= siz){ //out of bounds
//                    en = siz-1;
//                }
////                if(strt < lock_index){
////                    strt = lock_index + 1;
////                }
//
//                op = stringCheck(tmp_string.substr(strt,en-strt),en-strt);
//                if(op == '+'){
//                    lock_index = i;
//                }else if(op== '-'){
//                    if(en-strt == K )
//                        tmp_string = stringFilp(tmp_string,strt,K);
//                }
                //******************************************




            }
        }
        //cout<<endl<<input_string;
        //cout<<endl<<"Flips : "<<flips;
        //check last slot
        //cout<<"Helllloooo"<<stringCheck(input_string.substr(siz - K,K),K);
        //cout<<input_string.substr(siz - K,K);
        char check_ch = stringCheck(input_string.substr(siz - K,K),K);
        if(check_ch=='*'){
            not_possible=true;
        }
        cout<<endl<<not_possible;
        if(not_possible==false){
            //cout<<"Case #"<<tt<<": "<<flips<<endl;
            convert << tt;
            case_no = convert.str();
            convert.str("");
            convert.clear();

            convert << flips;
            answer = convert.str();
            convert.str("");
            convert.clear();
            output_string += "Case #"+case_no+": "+answer+"\n";


        }else{
            convert << tt;
            case_no = convert.str();
            convert.str("");
            convert.clear();
            //cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
            output_string += "Case #"+case_no+": "+"IMPOSSIBLE"+"\n";
        }
    }
    cout<<output_string;
    outfile<<output_string;
    outfile.close();
    return 0;
}
