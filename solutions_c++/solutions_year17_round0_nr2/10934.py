//
//  main.cpp
//  CodeJam1
//
//  Created by WangTing on 2017/4/8.
//  Copyright (c) 2017年 WangTing. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

void setArrayValue(char pArray[], int startIndex, int endIndex, char value);
void printArray(char pArray[], int length);
void computeTidy(char maxNumber[], char answer[]);
bool compareArray(char array1[], char array2[], int length);
string formattingAnswer(char charArray[], int length);

int main(int argc, const char * argv[]) {
    
    string testCase[100];
    int caseNumber=0;
    char maxNumber[19];
    char answer[19];
    
    cin >> caseNumber;
    
    for(int i=0; i<caseNumber;i++){
        
        // initial array value
        setArrayValue(maxNumber,0,18,'-');
        
        
        cin >> maxNumber;
        
        
        bool isFinish=false;
        while(isFinish==false){
            
            setArrayValue(answer,0,18,'-');
            answer[0]=maxNumber[0];
            
            computeTidy(maxNumber,answer);
            isFinish=compareArray(maxNumber,answer,19);
            
            copy(answer,answer + 19, maxNumber);
        }
        
        testCase[i]=formattingAnswer(answer,19);
        
    }
    
    
    
    for(int j=1;j<=caseNumber;j++){
        cout<<"Case #"<<j<<": "<<testCase[j-1]<<endl;
    }
    
    ofstream myfile;
    myfile.open ("output_file.txt");
    for(int j=1;j<=caseNumber;j++){
        myfile<<"Case #"<<j<<": "<<testCase[j-1]<<endl;
    }
    //myfile << "Writing this to a file.\n";
    myfile.close();
    
    
    return 0;
}

string formattingAnswer(char charArray[], int length){
    string value;
    for(int i=0; i<length; i++){
        if(charArray[i]!='-' && charArray[i]!='0'){
            value=value+charArray[i];
        }
    }
    return value;
}

void computeTidy(char maxNumber[], char answer[]){
    bool isDecompostion=false;
    
    for(int k=1;k<19;k++){
        
        if(maxNumber[k]=='-' ||maxNumber[k]=='\0'){
            break;
        }
        
        //後面比前面大(含相等) 順利填完
        if(maxNumber[k]>=maxNumber[k-1]){
            if(isDecompostion){
                answer[k]='9';
            }else{
                answer[k]=maxNumber[k];
            }
        }else{
            //後面比前面小
            if(isDecompostion==false){
                isDecompostion=true;
                int newNumber=answer[k-1]-'1';
                answer[k-1]='0'+newNumber;
            }
            answer[k]='9';
        }
    }
}

void printArray(char pArray[], int length) {
    for(int i=0; i<length; i++){
        cout<<pArray[i];
    }
    cout<<endl;
}

void setArrayValue(char pArray[], int startIndex, int endIndex, char value) {
    for(int i=startIndex; i<=endIndex; i++){
        pArray[i]=value;
    }
}

bool compareArray(char array1[], char array2[], int length){
    for(int i=0; i<length; i++){
        if(array1[i]!=array2[i]){
            return false;
        }
    }
    
    return true;
}

