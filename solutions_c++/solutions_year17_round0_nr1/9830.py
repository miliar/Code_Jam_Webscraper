//
//  main.cpp
//  Oversized_Pancake_Flipper
//
//  Created by Yip Martin on 2017-04-07.
//  Copyright © 2017 Yip Martin. All rights reserved.
//

#include <iostream>
using namespace std;




char fliping(char c){
    
    if (c == '+') {
        c = '-';
    }
    else if (c == '-'){
        c = '+';
    }
    
    return c;
}

int main(int argc, const char * argv[]) {
    int t,k;
    string s;
    int output[10];

    int positve = 0;
    int negative = 0;
    int flips = 0;
    int exceed = 0;
    cin >> t;
    
    for (int i = 1; i <= t; ++i) {
        
        flips = 0;
        negative=0;

        cin >> s;
        cin >> k;
        
        
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == '-'){
                flips++;
                
                /*
                //when it hasnt over the pancakes amount
                if ( (j+ k -1) <= ( s.length() - 1) ) {
                    
                    for (int l = 0; l < k; l++) {
                        s[j+l] = fliping(s[j+l]);
                    }
                   // s[j] = fliping(s[j]);
                    //s[j+1] = fliping(s[j+1]);
                    //s[j+2] =fliping(s[j+2]);
                    
                    cout <<  endl << "   check    " << endl;
                    
                    cout << s << endl;
                    
                    cout << "   check   end  " << endl;

                }
                
                //exceed 1
                else if ( (j+ k - 1) == (s.length() ))
                {
                    
                    for (int l = 0; l < k; l++) {
                        s[j+l -1] = fliping(s[j+l -1]);
                    }
                   // s[j-1] = fliping(s[j-1]);
                    //s[j] = fliping(s[j]);
                    //s[j+2] =fliping(s[j+2]);
                    
                    cout <<  endl << "   check    " << endl;
                    
                    cout << s << endl;
                    
                    cout << "   check   end  " << endl;
                }
                
                //exceed 2
                else if ((j+ k -1) == (s.length() + 1 )){
                    
                    for (int l = 0; l < k; l++) {
                        s[j+l -2] = fliping(s[j+l -2]);
                    }
                  //  s[j-2] =fliping(s[j-2]);
                    //s[j-1] = fliping(s[j-1]);
                    //s[j] = fliping(s[j]);
                    
                    cout <<  endl << "   check    " << endl;
                    
                    cout << s << endl;
                    
                    cout << "   check   end  " << endl;
                    }
                */
                exceed = j + k - 1 - (s.length());
                if (exceed < 0) {
                    exceed = 0;
                }
                
                for (int l = 0; l < k; l++) {
                    s[j+l - exceed] = fliping(s[j+l -exceed]);
                }
                
                
                
                
            }
            
        }
        
       /*cout <<  endl << "   check    " << endl;

        cout << s << endl;
        
        cout << "   check   end  " << endl;
        */
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == '-'){
                negative++;
            }
            
        }
        
      /*  cout << "Case #" << i << ": ";
        if (negative == 0) {
            cout << flips << endl;
        }
        else
            cout << "IMPOSSIBLE" << endl;
       */
        
        if(negative == 0)
        {
        output[i] = flips;
        }
        else
        output[i] = -1;
        
        
    }
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        if(output[i] == -1){
             cout << "IMPOSSIBLE" << endl;
        }
        else
            cout << output[i] << endl;
    }
    
    
    
    return 0;
}
