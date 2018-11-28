#include <QCoreApplication>
#include <QFile>
#include <QTextStream>
void splitPart(int * a, int * b, int len);
int minThing(int a, int b);
int maxThing(int a, int b);
int minThing(int a, int b){
    if(b < a)
        return b;
    return a;
}
int maxThing(int a, int b){
    if(b > a)
        return b;
    return a;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QFile input("input.in");
    if (!input.open(QIODevice::ReadOnly)) {

    }
    FILE * out = fopen("out.txt", "w");
    QTextStream reader(&input);
    reader.readLine();
    int ccase = 1;
    int len;
    int maxIndex, minIndex;
    int min, max;
    int splitA, splitB;
    int inMin, inMax;
    while(!reader.atEnd()){
        QString line = reader.readLine();
        fprintf(out, "Case #%d:", ccase++);
        QStringList parts = line.split(" ");
        QList<int> theParts;
        len = parts[0].toInt();
        theParts.push_back(len);
        for(int i = 0; i < parts[1].toInt(); i++){

            min = -1;
            max = -1;
            minIndex = maxIndex = 0;
            for(int t = 0; t < theParts.length(); t++){
                splitPart(&splitA, &splitB, theParts[t]);
                inMin = minThing(splitA, splitB);

                if(inMin > min){
                    inMax = maxThing(splitA, splitB);
                    maxIndex = t;
                    min = inMin;
                    max = inMax;
                }
                else if(inMin == min){
                    inMax = maxThing(splitA, splitB);
                    if(inMax > max){
                        maxIndex = t;
                        max = inMax;
                    }
                }
            }
            splitPart(&splitA, &splitB, theParts[maxIndex]);
            theParts.removeAt(maxIndex);
            if(splitA < 0)
                splitA = 0;
            if(splitB > 0)
                theParts.insert(maxIndex, splitB);
            if(splitA > 0)
                theParts.insert(maxIndex, splitA);

            if(i == (parts[1].toInt()-1)){
                fprintf(out," %d %d\n", splitB, splitA);

            }



        }


    }




    return a.exec();
}

void splitPart(int * a, int * b, int len){
    if(len % 2 == 0){
        *a = len / 2 - 1;
    }
    else{
        *a = len / 2;
    }
    *b = len /2 ;
}
