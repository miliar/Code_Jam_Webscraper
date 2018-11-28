// Acroph created at 2017-04-08 20:19:23
// ptx9363@gmail.com for more cantact

#include <iostream>
#define MAX_SIZE 100

using namespace std;


void printMap(char map[MAX_SIZE][MAX_SIZE], int n){
    cout << "=== Start Print Map ===" << endl;
    for(int i=0;i<n;i++) cout << "__";
    for(int i=0;i<n;i++){
        cout << endl <<  "|";
        for(int j=0;j<n;j++)
            cout << map[i][j] << " ";
        cout << "|" << endl;
    }
    cout << "======   Map End   ======" << endl;
}

int main(){
    int T;
    cin >> T;
    
    for(int t=0; t<T; t++){
        int N, M;

        cin >> N >> M;
        char map[MAX_SIZE][MAX_SIZE];
        for(int i=0;i<MAX_SIZE;i++) for(int j=0;j<MAX_SIZE;j++) map[i][j] = '.';
        char model;
        int row, col;

        for(int i=0;i<M;i++){
            cin >> model >> row >> col;
            map[row-1][col-1] = model;
        }
        
        char originalmap[MAX_SIZE][MAX_SIZE];
        for(int i=0;i<N;i++) for(int j=0;j<N;j++) originalmap[i][j] = map[i][j];

        // place able map
        char placablemap[MAX_SIZE][MAX_SIZE];
        bool found = true;
        
         // place '+'
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                placablemap[i][j] = map[i][j];
        
         for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                if (map[i][j] == '+' || map[i][j] == 'o'){
                    // clear diagonal 
                    for(int k=0;k<N;k++)
                        if (i+j-k >=0 && i+j-k<N && placablemap[k][i+j-k] == '.')
                            placablemap[k][i+j-k] = '*';
                    for(int k=0;k<N;k++)
                        if (k-i+j >=0 && k-i+j<N && placablemap[k][k-i+j] == '.')
                            placablemap[k][k-i+j] = '*';

                    /*
                    if (map[i][j] == 'o'){
                        for(int k=0;k<N;k++)
                            if (placablemap[i][k] == '.')
                                placablemap[i][k] = '*';
                        for(int k=0;k<N;k++)
                            if (placablemap[k][j] == '.')
                                placablemap[k][j] = '*';
                    }
                    */
                }
        
        
        int order[MAX_SIZE];
        for(int i=0;i<N;i++){
            if (i%2==0)
                order[i] = i / 2;
            else
                order[i] = N-1-i/2;
        }
        
        found = true;
        while(found){
            found = false;
            for(int ii=0;ii<N;ii++){
                int i = order[ii];
                for(int j=0;j<N;j++){
                    if (placablemap[i][j] == '.'){
                        // clear diagonal
                        map[i][j] = '+';
                        for(int k=0;k<N;k++)
                            if (i+j-k >=0 && i+j-k<N && placablemap[k][i+j-k] == '.')
                                placablemap[k][i+j-k] = '*';
                        for(int k=0;k<N;k++)
                            if (k-i+j >=0 && k-i+j<N && placablemap[k][k-i+j] == '.')
                                placablemap[k][k-i+j] = '*';
                        found = true;
                        break;
                    }
                }
                if (found)  break;
            }
        }

        //printMap(map, N);
        // select position for 'x'
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                placablemap[i][j] = map[i][j];
        
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                if (map[i][j] == 'x' || map[i][j] == 'o'){
                    // clear line
                    for(int k=0;k<N;k++)
                        if (placablemap[i][k] == '.')
                            placablemap[i][k] = '*';
                    for(int k=0;k<N;k++)
                        if (placablemap[k][j] == '.')
                            placablemap[k][j] = '*';
                    
                    /*
                    if (map[i][j] == 'o'){
                        for(int k=0;k<N;k++)
                            if (i+j-k >=0 && i+j-k<N && placablemap[k][i+j-k] == '.')
                                placablemap[k][i+j-k] = '*';
                        for(int k=0;k<N;k++)
                            if (k-i+j >=0 && k-i+j<N && placablemap[k][k-i+j] == '.')
                                placablemap[k][k-i+j] = '*';
 
                    }
                    */
                }
        
        found = true;
        while(found){
            found = false;
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    if (placablemap[i][j] == '.'){
                        // clear line
                        map[i][j] = 'x';
                        for(int k=0;k<N;k++)
                            if (placablemap[i][k] == '.')
                                placablemap[i][k] = '*';
                        for(int k=0;k<N;k++)
                            if (placablemap[k][j] == '.')
                                placablemap[k][j] = '*';
                        found = true;
                        break;
                    }
                }
                if (found)  break;
            }
        }
        
        
        //printMap(map, N);
       
        int count_x = 0;
        //count 'x'
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++)
                if (map[i][j] == 'x'){        
                   count_x++;
            }
        }

        char toChangeLabel = 'x';
        if (count_x < N)
            toChangeLabel = '+';
        
        found = true;
        while(found){
            found = false;
            for(int i=0;i<N;i++)
                for(int j=0;j<N;j++)
                if (map[i][j] == toChangeLabel){
                    //check line and diagonal
                    char temp = map[i][j];
                    map[i][j] = '.';

                    int valid = true;
                    for(int k=0;k<N;k++) if (i+j-k >=0 && i+j-k<N && (map[k][i+j-k] == '+' || map[k][i+j-k] == 'o')) valid = false;
                    for(int k=0;k<N;k++) if (k-i+j >=0 && k-i+j<N && (map[k][k-i+j] == '+' || map[k][k-i+j] == 'o')) valid = false;
                    for(int k=0;k<N;k++) if (map[i][k] == 'x' || map[i][k] == 'o') valid = false;
                    for(int k=0;k<N;k++) if (map[k][j] == 'x' || map[k][j] == 'o') valid = false;
                    
                    if (valid){
                        found = true;
                        map[i][j] = 'o';
                    }else{
                        map[i][j] = temp;
                    }
                     
                }
        }

        //printMap(originalmap, N);
        //printMap(map, N);

        int score = 0;
        int change_counter = 0;
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++){
                if (map[i][j] != originalmap[i][j])
                    change_counter++;
                
                if (map[i][j] == '+' || map[i][j] == 'x')
                    score++;
                if (map[i][j] == 'o')
                    score+=2;
            }
        
        cout << "Case #" << t+1 << ": " << score << " " << change_counter << endl;
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++){
                if (map[i][j] != originalmap[i][j]){
                    cout << map[i][j] << " " << i+1 << " " << j+1 << endl; 
                }
                
        }
    }


    return 0;
}
