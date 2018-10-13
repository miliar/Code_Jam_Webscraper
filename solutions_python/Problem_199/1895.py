import Foundation

var input = [String]()
var output = [String]()

func reading(){
  while let aux = readLine(){
    input.append(aux)
  }
}

func gettingLastChar(i: Int) -> String {
  var ans : String = ""
  for char in input[i].characters{
    if (char == "0" || char == "1" || char == "2" || char == "3" || char == "4" || char == "5" || char == "6" || char == "7" || char == "8" || char == "9"){
      ans += String(char)
    }
  }
  return ans
}

func getPanRowLength(i: Int) -> Int {
  var counter = 0
  for char in input[i].characters{
    if char == "-" || char == "+"{
      counter += 1
    }
  }
  return counter
}

func checkResult(i: Int, flipCounter: Int) -> String {
  for char in input[i].characters{
    if char == "-"{
      return "IMPOSSIBLE"
    }
  }
  return String(flipCounter)
}


func flipThoseCakes(i: Int, startIndex: Int) -> String {
  var str = input[i]
  let panFlipperLength = Int(gettingLastChar(i: i))!

  for pan in startIndex...(startIndex+panFlipperLength-1) {
    let index = str.index(str.startIndex, offsetBy: pan)
    if str[index] == "-" {
      str.remove(at: index)
      str.insert("+", at: index)
    }
    else{
      str.remove(at: index)
      str.insert("-", at: index)
    }
  }
  return str
}


func runThatRow(i: Int){
   var offset = 0
   var flipCounter = 0
   var rowLength = getPanRowLength(i: i)
    for char in 0...(rowLength-Int(gettingLastChar(i:i))!){
      var index = input[i].index(input[i].startIndex, offsetBy: offset)
      if input[i][index] != "+"{
        input[i] = flipThoseCakes(i: i, startIndex: offset)
        flipCounter += 1
      }
      offset += 1
    }

   output.append(checkResult(i: i, flipCounter: flipCounter))
}


func runGrid(){
  for row in 1...(Int(input[0])!) {
    runThatRow(i: row)
  }
}

func displayResult(){
  for row in 1...(Int(input[0])!) {
    print("Case #\(row): \(output[row-1])")
  }
}


func main(){
  reading()
  runGrid()
  displayResult()
  //runGrid()
  //writing()
  //print(input)
}


main()