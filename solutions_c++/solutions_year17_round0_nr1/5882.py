
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

static int case_count;
char const* input_path = "/Users/luna_z/Desktop/input.in";
char const* output_path = "/Users/luna_z/Desktop/output.out";


std::string func(char * s, int k){

    size_t ans = 0;
    size_t len = strlen(s);
    size_t p1 =0;
    
    do{
        if(s[p1] == '-'){
            if(p1 + k > len) return "IMPOSSIBLE";
            ans += 1;
            //flip next K
            for( int i = 0; i < k; i++){
                s[p1+i] = s[p1+i]=='+'?'-':'+';
            }
        }
        p1++;
    }while (p1 < len);
    
    return std::to_string(ans);
}

int main() {
    
    //read the input file and pass the arguemnt to function
    
    FILE *inf =fopen(input_path, "r");
    FILE *of = fopen(output_path, "w");
    fscanf(inf, "%d", &case_count);
    
    int cnt ;
    char arg1[1000];
    int arg2;
    for(cnt = 1; cnt < case_count + 1; cnt++){
        //parsing input
        fscanf(inf, "%s %d", arg1, &arg2);
        //write output
        fprintf(of, "Case #%d: %s\n", cnt, func(arg1, arg2).c_str());
    }
    
    fclose(inf);
    fclose(of);
    
    return 0;
}
