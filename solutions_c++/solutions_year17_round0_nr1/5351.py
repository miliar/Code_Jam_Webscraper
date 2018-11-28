
string flipper(string junk, unsigned long long int flipperSize){
    for(unsigned long long int i=0;i<flipperSize;i++){
        if(junk[i]=='-'){
            junk[i]='+';
        }
        else{
            junk[i]='-';
        }
    }
    return junk;
}

bool valid(string s, unsigned long long int k){
    for(unsigned long long int i=0;i<k;i++){
        if(s[s.length()-i-1]=='-')
            return false;
    }
    return true;
}


int writeFile ()
{
    unordered_map<int,int> a;
    ofstream myfile;
    ifstream myfile2;
    myfile2.open ("/Users/mac1/Desktop/anime/input.txt");
    myfile.open ("/Users/mac1/Desktop/anime/example.txt");
    
    //
    string s;
    unsigned long long int t, k, counter = 0;
    myfile2>>t;
    for(unsigned long long int j=0;j<t;j++){
        myfile2>>s>>k;
        counter = 0;
        for(unsigned long long int i=0;i<s.length();i++){
            string junk = s.substr(i, k);
            if(junk.length()==k){
                if(junk[0]=='-'){
                    junk = flipper(junk, k);
                    for(unsigned long long int z=0;z<k;z++){
                        s[i+z] = junk[z];
                    }
                    counter++;
                }
            }
        }
        if(valid(s,k))
            myfile<<"Case #"<<j+1<<": "<<counter<<endl;
        else
            myfile<<"Case #"<<j+1<<": IMPOSSIBLE"<<endl;
    }
    //
   
    myfile2.close();
    myfile.close();
    return 0;
}