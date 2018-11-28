
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

static int case_count;
char const* input_path = "/Users/luna_z/Desktop/input.in";
char const* output_path = "/Users/luna_z/Desktop/output.out";


std::string func(char * s){
    
    size_t len = strlen(s);
    
    //scan to right to see if there are flips
    int i = 0;
    int b = 0;
    
    while (i < len - 1) {
        i++;
        if(s[i] < s[i-1]){
            cout<<b<<endl;
            b = i;
            break;
        }
    }
    
    //original string is tidy
    if(b == 0) return s;
    
    for(i = b; i < len; i ++)
        s[i] = '9';
    s[b-1] -= 1;
    
    for(i = b - 1; i > 0; i--)
        if(s[i] < s[i-1]){
            s[i] = '9';
            s[i-1] -= 1;
        }
    if(s[0] =='0')
        s = &s[1];
    
    return s;
}

int main() {
    
    //read the input file and pass the arguemnt to function
    
    FILE *inf =fopen(input_path, "r");
    FILE *of = fopen(output_path, "w");
    fscanf(inf, "%d", &case_count);
    
    int cnt ;
    char arg1[20];
    for(cnt = 1; cnt < case_count + 1; cnt++){
        //parsing input
        fscanf(inf, "%s", arg1);
        //write output
        fprintf(of, "Case #%d: %s\n", cnt, func(arg1).c_str());
    }
    
    fclose(inf);
    fclose(of);
    
    return 0;
}
